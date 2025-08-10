from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.TaskListView.as_view(), name='task-list'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task-detail/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
]