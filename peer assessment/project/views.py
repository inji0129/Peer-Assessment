from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, CreatePollForm, CreatePeersForm, CreateCommentForm, CreateScoreForm
#from .filters import OrderFilter

from django.views.generic import TemplateView


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	return render(request,'dashboard.html')

@login_required(login_url='login')
def HomeView(request):
	polls = Poll.objects.all()
	comments = Comment.objects.all()
	context={
		'polls' : polls,
		'comments' : comments
	}
	return render(request, 'home.html', context)

@login_required(login_url='login')
def PeerView(request):
	peers = Peer.objects.all()
	context = {
		'peers' : peers
	}

	return render(request,'peers.html', context)

@login_required(login_url='login')
def create_peer(request):
	if request.method == 'POST':
		peer_form = CreatePeersForm(request.POST)
		if peer_form.is_valid():
			peer_form.save()
			return redirect('peers')
	else:
		peer_form = CreatePeersForm()

	context = {
		'peer_form' : peer_form
	}

	return render(request, 'peer_create.html', context)

@login_required(login_url='login')
def ScoreView(request):
	score = Score.objects.all()
	context = {
		'score' : score
	}

	return render(request,'score.html', context)


@login_required(login_url='login')
def create_score(request):
	if request.method == 'POST':
		score_form = CreateScoreForm(request.POST)
		if score_form.is_valid():
			score_form.save()
			return redirect('scores')
	else:
		score_form = CreateScoreForm()

	context = {
		'score_form' : score_form
	}

	return render(request, 'score_create.html', context)



@login_required(login_url='login')
def create(request):
	if request.method == 'POST':
		form = CreatePollForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('homeview')
	else:
		form = CreatePollForm()
	context = {
		'form' : form
	}

	return render(request, 'create.html', context)

@login_required(login_url='login')
def create_comment(request):
	if request.method == 'POST':
		form = CreateCommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('homeview')
	else:
		form = CreateCommentForm()
	context = {
		'form' : form
	}

	return render(request, 'create_comment.html', context)

@login_required(login_url='login')
def vote(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)

	if request.method == 'POST':
		selected_option = request.POST['poll']
		if selected_option == 'option1':
			poll.option_one_count += 5
			poll.option_two_count = 0
			poll.option_three_count = 0
			poll.option_four_count = 0
			poll.option_five_count = 0

		elif selected_option == 'option2':
			poll.option_two_count += 4
			poll.option_one_count = 0
			poll.option_three_count = 0
			poll.option_four_count = 0
			poll.option_five_count = 0

		elif selected_option == 'option3':
			poll.option_three_count += 3
			poll.option_one_count = 0
			poll.option_two_count = 0
			poll.option_four_count = 0
			poll.option_five_count = 0

		elif selected_option == 'option4':
			poll.option_four_count += 2
			poll.option_one_count = 0
			poll.option_two_count = 0
			poll.option_three_count = 0
			poll.option_five_count = 0

		elif selected_option == 'option5':
			poll.option_five_count += 1
			poll.option_one_count = 0
			poll.option_two_count = 0
			poll.option_three_count = 0
			poll.option_four_count = 0

		else:
			return HttpResponse(400, 'Invalid form')

		poll.save()


		return redirect('results', poll.id)

	context = {
		'poll' : poll

	}
	return render(request, 'vote.html', context)

def comment(request, poll_id):
	comment = Comment.objects.get(pk=poll_id)
	if request.method == 'POST':
		
		comment.save()

		return redirect('result', comment.id)

	context = {
		'comment' : comment
	}
	return render(request, 'comment.html', context)

@login_required(login_url='login')
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)


    context = {
        'poll' : poll,

    }
    return render(request, 'results.html', context)



@login_required(login_url='login')
def result(request, poll_id):
    comment = Comment.objects.get(pk=poll_id)


    context = {
        'comment' : comment,

    }
    return render(request, 'result.html', context)
