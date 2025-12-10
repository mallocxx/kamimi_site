#!/bin/bash

# Скрипт для запуска проекта

echo "🚀 Запуск CTF Competition Site на 127.0.0.1..."

# Запуск backend в фоне
echo "📦 Запуск Flask backend на https://127.0.0.1:5000..."
python3 app.py &
BACKEND_PID=$!

# Ждем немного, чтобы backend запустился
sleep 3

# Запуск frontend
echo "🎨 Запуск Vue frontend на http://127.0.0.1:5173..."
npm run dev

# При завершении убиваем backend процесс
trap "kill $BACKEND_PID 2>/dev/null" EXIT

