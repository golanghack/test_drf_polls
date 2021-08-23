from rest_framework import generics 
from polls.models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

class PollAPIView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceAPIView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class VoteAPIView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer