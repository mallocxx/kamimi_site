#!/bin/bash

# Скрипт для запуска проекта

echo "🚀 Запуск CTF Competition Site на 127.0.0.1..."

# Запуск PHP backend (mail) через Docker Compose
echo "📦 Запуск PHP backend (mail) на http://127.0.0.1:8080..."
cd mail
sudo docker compose up -d
cd ..

# Ждем немного, чтобы backend запустился
sleep 5

# Запуск frontend
echo "🎨 Запуск Vue frontend на http://127.0.0.1:5173..."
npm run dev

# При завершении останавливаем backend контейнеры
trap "cd mail && docker compose down 2>/dev/null" EXIT

