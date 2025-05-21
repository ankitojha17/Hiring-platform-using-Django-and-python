from django.db import models
from hr.models import JobPost , CandidateApplications
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from django.db import models
from hr.models import JobPost



class MyApplyJobList(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    job = models.ForeignKey(to=CandidateApplications,on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)


class IsSortList(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    job = models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)


class Bookmark(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job')

    def __str__(self):
        return f"{self.candidate} bookmarked {self.job}"

