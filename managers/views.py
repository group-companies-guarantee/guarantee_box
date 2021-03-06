from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Manager
from students.models import Teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

@login_required(login_url='/accounts/login/')
def manager(request):
    return render(request, 'managers/main/profile.html', {"manager": 'sasdasd'})


class ApplicantListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'managers/main/profile.html'
    queryset = Teacher.objects.filter(status__name='Applicant')
    context_object_name = 'applicant_list'


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'managers/main/teachers.html'
    queryset = Teacher.objects.filter(status__name='Teacher')
    context_object_name = 'teacher_list'