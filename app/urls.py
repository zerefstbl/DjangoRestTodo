from django.urls import path
from . import views

urlpatterns = [
  path('', views.TodoListView.as_view()),
  path('<int:pk>', views.TodoEditAndDeleteView.as_view())
]
