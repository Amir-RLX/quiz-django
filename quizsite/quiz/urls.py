from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz-maker/', views.CreateQuizForm.as_view(), name="quiz"),

]
