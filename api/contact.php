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

// Production handoff: connect this validated payload to the CRM/email provider of choice.
// Do not store client data in the serverless filesystem; it is ephemeral.
http_response_code(200);
echo json_encode(['ok' => true, 'message' => 'Thanks — your brief is ready for the CartMakers team.', 'received' => ['name' => $name, 'email' => $email, 'company' => $company]]);
