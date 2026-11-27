from .views import ExerciseAPIView

from django.urls import path

urlpatterns = [
    path('exercises/', ExerciseAPIView.as_view(), name='exercise-list'),
    path('exercises/<int:id>/', ExerciseAPIView.as_view(), name='exercise-detail'),
]
