# Инструкция по развертыванию на 127.0.0.1

## Быстрый запуск

### Вариант 1: Используя скрипт
```bash
./start.sh
```

### Вариант 2: Вручную (в двух терминалах)

**Терминал 1 - Backend (mail, PHP + nginx через Docker Compose):**
```bash
cd mail
docker compose up -d
```
Backend будет доступен на: `http://127.0.0.1:8080`

**Терминал 2 - Frontend (Vite dev):**
```bash
npm run dev
```
Frontend будет доступен на: `http://127.0.0.1:5173`

## Доступ к сайту

После запуска откройте в браузере:
- **Frontend (dev)**: http://127.0.0.1:5173
- **Backend API (mail/nginx)**: http://127.0.0.1:8080

**Важно**: Backend из каталога `mail` поднимается через Docker Compose (nginx + php-fpm + PHPMailer). Для продакшена используйте Nginx + Let’s Encrypt (см. пример конфигурации в README.md).

## Настройка email (опционально)

Если хотите получать email уведомления о регистрациях (через PHPMailer, SMTP Яндекса по умолчанию):

1. В файле `mail/docker-compose.yml` задайте переменные окружения:
```
SMTP_USERNAME=your-email@example.com
SMTP_PASSWORD=your-app-password
```
2. Перезапустите backend:
```bash
cd mail
docker compose down
docker compose up -d
```

## Остановка серверов

- Если используете скрипт `start.sh`: нажмите `Ctrl+C` (frontend остановится), затем:
```bash
cd mail && docker compose down
```
- Если запускали вручную: `Ctrl+C` в терминале с `npm run dev` и `docker compose down` в каталоге `mail`

