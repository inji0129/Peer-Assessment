
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('form/', views.HomeView, name='homeview'),
	path('create/', views.create, name='create'),
	path('create_comment/', views.create_comment, name='create_comment'),
	path('vote/<poll_id>/', views.vote, name='vote'),
	path('comment/<poll_id>/', views.comment, name='comment'),
	path('results/<poll_id>/', views.results, name='results'),
	path('result/<poll_id>/', views.result, name='result'),
	path('peers/', views.PeerView, name='peers'),
	path('peer_create/', views.create_peer, name='create_peer'),
	path('scores/', views.ScoreView, name='scores'),
	path('score_create/', views.create_score, name='create_score'),

    path('', views.home, name="home"),

	path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "password_reset.html"), name="reset_password"),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name = "password_reset_done"),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name = "password_reset_confirm"),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name = "password_reset_complete"),

]
