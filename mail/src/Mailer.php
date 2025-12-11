<?php

namespace App;

use PHPMailer\PHPMailer\PHPMailer;

class Mailer
{
    private PHPMailer $mailer;

    public function __construct()
    {
        $this->mailer = new PHPMailer(true);

        // SMTP Яндекса
        $this->mailer->isSMTP();
        $this->mailer->Host       = 'smtp.yandex.ru';
        $this->mailer->SMTPAuth   = true;

        $this->mailer->Username   = getenv('SMTP_USERNAME');
        $this->mailer->Password   = getenv('SMTP_PASSWORD');

        $this->mailer->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $this->mailer->Port       = 587;

        $this->mailer->CharSet    = 'UTF-8';

        $this->mailer->setFrom(getenv('SMTP_USERNAME'), 'Форма с сайта');
    }

    public function sendFormData(
        string $name,
        string $email,
        string $experience,
        string $extra
    ): void {
        $this->mailer->clearAllRecipients();
        $this->mailer->addAddress(getenv('SMTP_USERNAME'));

        $this->mailer->Subject = 'Новая заявка с формы';

        $body =
            "Имя: {$name}\n" .
            "Email: {$email}\n" .
            "Уровень опыта: {$experience}\n" .
            "Доп. информация: {$extra}\n";

        $this->mailer->Body = $body;

        $this->mailer->send();
    }
}
