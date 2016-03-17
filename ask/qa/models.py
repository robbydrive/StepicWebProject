from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
   title = models.CharField(max_length=255)
   text = models.TextField()
   added_at = models.DateTimeField()
   rating = models.IntegerField(default=0)
   author = models.ForeignKey(User, related_name="questions")
   likes = models.ManyToManyField(User)
   class Meta:
      db_table = "qa_questions"

class Answer(models.Model):
   text = models.TextField()
   added_at = models.DateTimeField()
   question = models.ForeignKey(Question)
   author = models.ForeignKey(User, related_name="answers")
   class Meta:
      db_table = "qa_answers"
