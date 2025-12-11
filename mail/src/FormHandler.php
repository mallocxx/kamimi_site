<?php

namespace App;

class FormHandler
{
    private Mailer $mailer;

    public function __construct(Mailer $mailer)
    {
        $this->mailer = $mailer;
    }

    public function handle(): void
    {
        // CORS headers
        header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Methods: POST, OPTIONS');
        header('Access-Control-Allow-Headers: Content-Type');
        header('Content-Type: application/json; charset=utf-8');

        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            http_response_code(405);
            echo json_encode(['error' => 'Method not allowed']);
            return;
        }

        $data = $_POST;

        if (empty($data)) {
            $raw = file_get_contents('php://input') ?: '';
            $decoded = json_decode($raw, true);
            if (is_array($decoded)) {
                $data = $decoded;
            }
        }

        $name       = $data['name']       ?? '';
        $email      = $data['email']      ?? '';
        $experience = $data['experience'] ?? '';
        $extra      = $data['extra']      ?? '';

        try {
            $this->mailer->sendFormData($name, $email, $experience, $extra);
            echo json_encode(['status' => 'ok']);
        } catch (\Throwable $e) {
            http_response_code(500);
            echo json_encode([
                'status'  => 'error',
                'error'   => $e->getMessage()
            ]);
        }
    }
}
