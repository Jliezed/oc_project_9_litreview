from django import forms
from .models import Ticket, Review, UserFollows
from user.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

class TicketForm(forms.ModelForm):
    title = forms.CharField(label="Titre")
    class Meta:
        model = Ticket
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    rating = forms.ChoiceField(
        label="Note",
        widget=forms.RadioSelect, choices=RATING_CHOICES)

    headline = forms.CharField(label="Titre")
    body = forms.CharField(widget=forms.Textarea, label="Commentaire")

    class Meta:
        model = Review
        exclude = ('user', 'time_created', 'ticket',)


User = get_user_model()
class FollowUsersForm(forms.ModelForm):
    followed_user = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur"}))

    # Clean the input received for followed user field
    def clean_followed_user(self):
        data = self.cleaned_data["followed_user"]
        # Transform the string to CustomUser Object

        followed_user = CustomUser.objects.get(username__exact=data)
        return followed_user


    class Meta:
        model = UserFollows
        fields = ['followed_user']

