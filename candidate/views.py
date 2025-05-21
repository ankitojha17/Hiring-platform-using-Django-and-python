from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications
from candidate.models import MyApplyJobList
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from hr.models import JobPost
from .models import Bookmark

@login_required
def candidateHome(request):
    jobpost = JobPost.objects.all()
    return render(request,'candidate/dashboradh.html',{'jobpost':jobpost})

@login_required
def applyJob(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        yearOfExperience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')
        job = JobPost.objects.get(id=id)
        if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            return redirect('dash')
        CandidateApplications(user=request.user,job=job,passingYear=passing_year,yearOfExperience=yearOfExperience,resume=resume).save()
        return redirect('dash')
    return render(request,'candidate/apply.html')

@login_required
def myjoblist(request):
    joblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})

@login_required
def add_bookmark(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    Bookmark.objects.get_or_create(candidate=request.user, job=job)
    return redirect('job_detail', job_id=job.id)  # Redirect to job detail page after bookmarking

@login_required
def remove_bookmark(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    Bookmark.objects.filter(candidate=request.user, job=job).delete()
    return redirect('job_detail', job_id=job.id)  # Redirect to job detail page after removing bookmark

@login_required
def view_bookmarks(request):
    bookmarks = Bookmark.objects.filter(candidate=request.user).select_related('job')
    return render(request, 'candidate/bookmarks.html', {'bookmarks': bookmarks})
