import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Model definition for Question.
    """

    question_text = models.CharField('Question', max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def was_published_recently(self):
        """
        Checks whether Question Was published in the last 24hrs
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        """
        Unicode representation of Question.
        """
        return self.question_text


class Choice(models.Model):
    """
    Model definition for Choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Unicode representation of Choice.
        """
        return f"{self.choice_text} has {self.votes} votes"
