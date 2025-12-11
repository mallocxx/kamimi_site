FROM php:8.2-fpm-alpine

WORKDIR /var/www/html

# Подтягиваем composer из официального образа
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

CMD ["php-fpm"]
