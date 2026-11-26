from .views import ExerciseAPIView

from django.urls import path

urlpatterns = [
    path('exercises/', ExerciseAPIView.as_view(), name='exercise-api'),
]
