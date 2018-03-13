from django.contrib import admin
from blog.models import Articles

# Добавили таблицу в панель администратора
admin.site.register(Articles)