# CTF Competition Landing Page

Одностраничный сайт-визитка для регистрации на CTF соревнования с отправкой email уведомлений.

## Технологии

- **Frontend**: Vue 3 + Tailwind CSS
- **Backend**: PHP (PHPMailer) в каталоге `mail/`, поднимается через Docker Compose (nginx + php-fpm)
- **Email**: SMTP (по умолчанию пример с Яндекс, можно заменить на свой)

## Установка

### Backend (mail)
```bash
cd mail
docker compose up -d
```
Переменные окружения для SMTP задаются в `mail/docker-compose.yml` (`SMTP_USERNAME`, `SMTP_PASSWORD`).

### Frontend
```bash
npm install
```

## Запуск (dev)

1) Backend (mail):
```bash
cd mail
docker compose up -d
```

2) Frontend:
```bash
npm run dev
```

## Продакшен

Рекомендуется разместить собранный фронтенд как статику за Nginx и проксировать `/api` на PHP (nginx + php-fpm). Сертификаты — через Let's Encrypt (`certbot --nginx -d your-domain.com`).

## Структура проекта

```
kamimi_site/
├── src/              # Vue frontend
│   ├── App.vue      # Главный компонент
│   ├── main.js      # Точка входа
│   └── style.css    # Стили
├── mail/            # PHP backend (nginx + php-fpm + PHPMailer)
│   ├── public/      # index.php — точка входа API
│   ├── src/         # FormHandler.php, Mailer.php
│   ├── docker-compose.yml
│   └── nginx/       # default.conf
├── package.json     # Node зависимости
└── README.md
```

## Особенности

- ✅ Отправка email уведомлений организатору
- ✅ Современный дизайн с градиентами и анимациями
- ✅ Адаптивная верстка
- ✅ Валидация форм

