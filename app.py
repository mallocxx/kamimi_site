from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://127.0.0.1:5173"}})

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
ORGANIZER_EMAIL = os.getenv('ORGANIZER_EMAIL', '')
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')

def send_registration_email(participant_data):
    """Отправляет email организатору с информацией о регистрации"""
    # Проверяем наличие необходимых настроек
    if not SMTP_USERNAME or not SMTP_PASSWORD or not ORGANIZER_EMAIL:
        return True
    
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = ORGANIZER_EMAIL
        msg['Subject'] = f'Новая регистрация на CTF: {participant_data["name"]}'
        
        body = f"""
        Новая регистрация на CTF соревнование!
        
        Информация об участнике:
        -------------------------
        Имя: {participant_data['name']}
        Email: {participant_data['email']}
        Уровень опыта: {participant_data.get('experience', 'Не указан')}
        Дополнительная информация: {participant_data.get('message', 'Нет')}
        
        -------------------------
        Дата регистрации: {participant_data.get('timestamp', 'N/A')}
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        
        return True
    except Exception:
        return True

@app.route('/api/register', methods=['POST', 'OPTIONS'])
def register():
    # Обработка preflight запросов CORS
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    
    try:
        data = request.get_json(force=True, silent=True)
        
        if not data or not isinstance(data, dict):
            return jsonify({'error': 'Отсутствуют данные для регистрации'}), 400
        
        # Валидация обязательных полей
        name = (data.get('name') or '').strip()
        email = (data.get('email') or '').strip()
        
        if not name or not email:
            return jsonify({'error': 'Имя и email обязательны для заполнения'}), 400
        
        # Добавляем timestamp
        from datetime import datetime
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Отправляем email
        try:
            send_registration_email(data)
        except Exception:
            pass
        
        response = jsonify({
            'success': True,
            'message': 'Регистрация успешна!'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
            
    except Exception as e:
        error_response = jsonify({'error': 'Внутренняя ошибка сервера'})
        error_response.headers.add('Access-Control-Allow-Origin', '*')
        return error_response, 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        ssl_context='adhoc',
        debug=True
    )

