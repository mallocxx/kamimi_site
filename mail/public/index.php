<?php

declare(strict_types=1);

require __DIR__ . '/../vendor/autoload.php';

use App\Mailer;
use App\FormHandler;

// CORS headers
header('Access-Control-Allow-Origin: http://127.0.0.1:5173');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Max-Age: 86400');

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$handler = new FormHandler(new Mailer());
$handler->handle();
