from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
   title = models.CharField(max_length=255, default="")
   text = models.TextField(default="")
   added_at = models.DateTimeField(auto_now_add=True)
   rating = models.IntegerField(default=0)
   author = models.ForeignKey(User, related_name="questions", default=1)
   likes = models.ManyToManyField(User)
   class Meta:
      db_table = "qa_questions"

class Answer(models.Model):
   text = models.TextField(default="")
   added_at = models.DateTimeField(auto_now_add=True)
   question = models.ForeignKey(Question)
   author = models.ForeignKey(User, related_name="answers", default=1)
   class Meta:
      db_table = "qa_answers"
