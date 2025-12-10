# CTF Competition Landing Page

Одностраничный сайт-визитка для регистрации на CTF соревнования с HTTPS поддержкой и отправкой email уведомлений.

## Технологии

- **Frontend**: Vue 3 + Tailwind CSS
- **Backend**: Flask (Python)
- **HTTPS**: TLS/SSL сертификаты
- **Email**: SMTP через TLS

## Установка

### Backend

1. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` на основе `.env.example` и заполните данные для отправки email:
```bash
cp .env.example .env
```

Для Gmail нужно использовать App Password вместо обычного пароля.

### Frontend

1. Установите зависимости:
```bash
npm install
```

## Запуск

### Разработка

1. Запустите backend (в одном терминале):
```bash
python app.py
```

2. Запустите frontend (в другом терминале):
```bash
npm run dev
```

При первом запуске Flask создаст самоподписанный SSL сертификат для разработки.

### Продакшен

Для продакшена рекомендуется использовать:

1. **Nginx** как reverse proxy с Let's Encrypt сертификатами
2. **Gunicorn** для запуска Flask приложения
3. Настоящие SSL сертификаты от Let's Encrypt

Пример конфигурации Nginx:
```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5173;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Структура проекта

```
kamimi_site/
├── src/              # Vue frontend
│   ├── App.vue      # Главный компонент
│   ├── main.js      # Точка входа
│   └── style.css    # Стили
├── app.py           # Flask backend
├── requirements.txt # Python зависимости
├── package.json     # Node зависимости
└── .env            # Конфигурация (не в git)
```

## Особенности

- ✅ HTTPS/TLS защищенное соединение
- ✅ Отправка email уведомлений организатору
- ✅ Современный дизайн с градиентами и анимациями
- ✅ Адаптивная верстка
- ✅ Валидация форм

