from operator import mod
from django.db import models
from users.models import Profile
# Create your models here.
class PollQuestion(models.Model):
    username=models.OneToOneField(Profile, on_delete=models.CASCADE,null=True)
    question=models.TextField(max_length=500)
    first=models.CharField(max_length=250)
    second=models.CharField(max_length=250)
    third=models.CharField(max_length=250)
    fourth=models.CharField(max_length=250)

    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    created_at=models.DateTimeField(null=True)


    def __str__(self):
        return self.question

    def total(self):
        return self.option_one_count+self.option_two_count+self.option_three_count+self.option_four_count

# class PollAnswers(models.Model):
#     answers=models.CharField(max_length=500)
#     question=models.ForeignKey(PollQuestion,on_delete=models.CASCADE)
