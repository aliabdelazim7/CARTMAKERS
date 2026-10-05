<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
  http_response_code(405);
  echo json_encode(['ok' => false, 'message' => 'Method not allowed']);
  exit;
}

$body = json_decode(file_get_contents('php://input'), true) ?: $_POST;
$name = trim((string)($body['name'] ?? ''));
$email = trim((string)($body['email'] ?? ''));
$company = trim((string)($body['company'] ?? ''));
$message = trim((string)($body['message'] ?? ''));

if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || $message === '') {
  http_response_code(422);
  echo json_encode(['ok' => false, 'message' => 'Please provide a name, valid email, and project brief.']);
  exit;
}

$botToken = (string)(getenv('TELEGRAM_BOT_TOKEN') ?: '');
$chatId = (string)(getenv('TELEGRAM_CHAT_ID') ?: '');
if ($botToken === '' || $chatId === '') {
  error_log('Telegram contact integration is not configured.');
  http_response_code(503);
  echo json_encode(['ok' => false, 'message' => 'The contact channel is temporarily unavailable.']);
  exit;
}

$escape = static fn(string $value): string => htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
$text = implode("\n", [
  '<b>رسالة جديدة من موقع CartMakers</b>',
  '',
  '<b>الاسم:</b> ' . $escape($name),
  '<b>البريد:</b> ' . $escape($email),
  '<b>الشركة:</b> ' . $escape($company !== '' ? $company : 'غير مذكور'),
  '<b>الرسالة:</b>',
  $escape($message),
]);

$telegramUrl = 'https://api.telegram.org/bot' . rawurlencode($botToken) . '/sendMessage';
$requestBody = http_build_query([
  'chat_id' => $chatId,
  'text' => $text,
  'parse_mode' => 'HTML',
  'disable_web_page_preview' => 'true',
]);
$requestContext = stream_context_create(['http' => [
  'method' => 'POST',
  'header' => "Content-Type: application/x-www-form-urlencoded\r\nContent-Length: " . strlen($requestBody),
  'content' => $requestBody,
  'timeout' => 10,
  'ignore_errors' => true,
]]);
$response = @file_get_contents($telegramUrl, false, $requestContext);
$status = 0;
foreach (($http_response_header ?? []) as $header) {
  if (preg_match('/^HTTP\/\S+\s+(\d+)/', $header, $matches)) {
    $status = (int)$matches[1];
    break;
  }
}

$telegram = is_string($response) ? json_decode($response, true) : null;
if ($status < 200 || $status >= 300 || !is_array($telegram) || empty($telegram['ok'])) {
  error_log('Telegram delivery failed: HTTP ' . $status);
  http_response_code(502);
  echo json_encode(['ok' => false, 'message' => 'Could not deliver the brief. Please try again.']);
  exit;
}

http_response_code(200);
echo json_encode([
  'ok' => true,
  'message' => 'Thanks — your brief was sent to the CartMakers team.',
  'received' => ['name' => $name, 'email' => $email, 'company' => $company],
]);
