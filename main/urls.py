from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/new/', views.todo_new, name='todo_new'),
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('user/', views.todo_user, name='todo-user'),
]