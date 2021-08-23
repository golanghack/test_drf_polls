from django.urls import path 
from .views import PollAPIView, ChoiceAPIView, VoteAPIView



urlpatterns = [
    path('', PollAPIView.as_view()),
    path('choices/', ChoiceAPIView.as_view()),
    path('votes/', VoteAPIView.as_view()),
]