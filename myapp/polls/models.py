from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# 
# (DATABASE PURSOSE)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #include the __str__inbuilt function for your own convinience
    def __str__(self):
        return self.question_text
    #custom method to this model
    def was_recently_published(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
class Choice(models.Model):
    #creating a relation between question and choices
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #include the __str__inbuilt function for your own convinience
    def __str__(self):
        return self.choice_text
#we need our polls app installed in the settings.py file
#open the settings.py file and include it among installed apps

'''
summary
>Changeyourmodels(in models.py).
>Run python manage.pymakemigrations tocreatemigrationsforthosechanges
>Run python manage.pymigrate toapplythosechangestothedatabase.

'''
