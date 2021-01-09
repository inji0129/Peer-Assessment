
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe


from .models import Poll, Peer, Comment, Score



class CreateUserForm(UserCreationForm):
	eagleID = forms.CharField(required=True)
	FirstName = forms.CharField(required=True)
	LastName = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ['username', 'FirstName', 'LastName', 'email', 'eagleID', 'password1', 'password2']

	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.eagleID = self.cleaned_data["eagleID"]
		user.FirstName = self.cleaned_data["FirstName"]
		user.LastName = self.cleaned_data["LastName"]
		if commit:
			user.save()
		return user

class CreatePollForm(ModelForm):
	class Meta:
		model = Poll
		fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'option_five']

class CreateCommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['question', 'comment_one']

class CreateScoreForm(ModelForm):
	class Meta:
		model = Score
		fields = ['total_score', 'total_question', 'total_student']

class CreatePeersForm(ModelForm):
	class Meta:
		model= Peer
		fields = ['name']
