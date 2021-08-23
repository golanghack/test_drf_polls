from rest_framework import serializers 
from polls.models import Poll, Choice, Vote


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('owner', 'text', 'pub_date', 'active')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice 
        fields = ('poll', 'choice_text')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('user', 'poll', 'choice')