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

$ch = curl_init('https://api.telegram.org/bot' . rawurlencode($botToken) . '/sendMessage');
curl_setopt_array($ch, [
  CURLOPT_POST => true,
  CURLOPT_POSTFIELDS => http_build_query([
    'chat_id' => $chatId,
    'text' => $text,
    'parse_mode' => 'HTML',
    'disable_web_page_preview' => 'true',
  ]),
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CONNECTTIMEOUT => 5,
  CURLOPT_TIMEOUT => 10,
]);
$response = curl_exec($ch);
$curlError = curl_error($ch);
$status = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$telegram = is_string($response) ? json_decode($response, true) : null;
if ($curlError !== '' || $status < 200 || $status >= 300 || !is_array($telegram) || empty($telegram['ok'])) {
  error_log('Telegram delivery failed: ' . ($curlError !== '' ? $curlError : ('HTTP ' . $status)));
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
