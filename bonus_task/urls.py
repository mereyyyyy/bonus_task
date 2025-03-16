from django.contrib import admin
from django.urls import path, include  # 🔹 Добавлен import path и include
from django.shortcuts import redirect  # 🔹 Добавлен import redirect

urlpatterns = [
    path('', lambda request: redirect('/notes/')),  # 🔹 Редирект на /notes/
    path('admin/', admin.site.urls),
    path('notes/', include('note.urls')),  # 🔹 Убедись, что у тебя есть note.urls
]
