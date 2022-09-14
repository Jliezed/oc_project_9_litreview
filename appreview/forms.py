from django import forms
from .models import Ticket, Review
from django.contrib.auth import get_user_model


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = '__all__'
        exclude = ('user',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'time_created', 'ticket',)


class ReviewExistingTicketForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'time_created','ticket',)


User = get_user_model()
class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
