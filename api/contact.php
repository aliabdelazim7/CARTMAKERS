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
$phone = trim((string)($body['phone'] ?? ''));
$projectType = trim((string)($body['project_type'] ?? ''));
$budget = trim((string)($body['budget'] ?? ''));
$timeline = trim((string)($body['timeline'] ?? ''));
$message = trim((string)($body['message'] ?? ''));
$website = trim((string)($body['website'] ?? ''));
$package = is_array($body['package'] ?? null) ? $body['package'] : [];
$addons = is_array($body['addons'] ?? null) ? $body['addons'] : [];
$estimatedTotal = is_numeric($body['estimated_total'] ?? null) ? (float)$body['estimated_total'] : 0;
$diagnostic = is_array($body['diagnostic'] ?? null) ? $body['diagnostic'] : [];

if ($website !== '') {
  http_response_code(422);
  echo json_encode(['ok' => false, 'message' => 'Invalid submission.']);
  exit;
}
if (mb_strlen($name) > 100 || mb_strlen($email) > 160 || mb_strlen($company) > 160 || mb_strlen($phone) > 40 || mb_strlen($projectType) > 100 || mb_strlen($budget) > 100 || mb_strlen($timeline) > 100 || mb_strlen($message) > 3000 || $name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || mb_strlen($message) < 10) {
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
$packageLabel = trim((string)($package['platform'] ?? '') . ' — ' . (string)($package['name'] ?? ''));
$addonLabels = array_values(array_filter(array_map(static function ($addon) use ($escape) {
  if (!is_array($addon)) return null;
  $addonName = trim((string)($addon['name'] ?? ''));
  if ($addonName === '') return null;
  $price = is_numeric($addon['price'] ?? null) && (float)$addon['price'] > 0 ? ' (+ ' . number_format((float)$addon['price'], 0) . ' EGP)' : ' (حسب النطاق)';
  return $escape($addonName . $price);
}, $addons)));
$selectionLines = [];
if ($packageLabel !== ' — ') $selectionLines[] = '<b>الباقة:</b> ' . $escape($packageLabel);
if ($addonLabels) $selectionLines[] = '<b>الإضافات:</b> ' . implode('، ', $addonLabels);
if ($estimatedTotal > 0) $selectionLines[] = '<b>الإجمالي المبدئي:</b> ' . number_format($estimatedTotal, 0) . ' جنيه';
if (!empty($diagnostic['recommendation'])) $selectionLines[] = '<b>نتيجة التشخيص:</b> ' . $escape((string)$diagnostic['recommendation']);
if (!empty($diagnostic['insight'])) $selectionLines[] = '<b>Insight:</b> ' . $escape((string)$diagnostic['insight']);
$text = implode("\n", [
  '<b>رسالة جديدة من موقع CartMakers</b>',
  '',
  '<b>الاسم:</b> ' . $escape($name),
  '<b>البريد:</b> ' . $escape($email),
  '<b>الشركة:</b> ' . $escape($company !== '' ? $company : 'غير مذكور'),
  '<b>واتساب:</b> ' . $escape($phone !== '' ? $phone : 'غير مذكور'),
  '<b>نوع الطلب:</b> ' . $escape($projectType !== '' ? $projectType : 'غير محدد'),
  '<b>الميزانية:</b> ' . $escape($budget !== '' ? $budget : 'غير محددة'),
  '<b>التوقيت:</b> ' . $escape($timeline !== '' ? $timeline : 'غير محدد'),
  ...$selectionLines,
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
