from django.db import models

# Create your models here.

class Poll(models.Model):
	question = models.TextField()
	option_one = models.CharField(max_length=30)
	option_two = models.CharField(max_length=30)
	option_three = models.CharField(max_length=30)
	option_four = models.CharField(max_length=30)
	option_five = models.CharField(max_length=30)
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)
	option_four_count = models.IntegerField(default=0)
	option_five_count = models.IntegerField(default=0)


	def total(self):
		return (self.option_one_count ) + (self.option_two_count) + (self.option_three_count)+ (self.option_four_count)+ (self.option_five_count)

class Score(models.Model):
	total_score = models.IntegerField(default=0)
	total_question = models.IntegerField(default=0)
	total_student = models.IntegerField(default=0)

	def total(self):
		return (((self.total_score/ self.total_student.count)/ (5 * self.total_question) ) * 100)


class Comment(models.Model):
	question = models.TextField()
	comment_one = models.TextField()

	def __str__(self):
		return self.comment_one

class Peer(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name
