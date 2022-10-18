import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all().order_by('position'),
    }
    return render(request, template_name='resume/index.html', context=context)


def projectview(request, pk):
    project = Project.objects.get(id=pk)
    project_images = ProjectImage.objects.filter(project=project)

    context = {
        'project': project,
        'project_images': project_images
    }
    return render(request, template_name='resume/portfolio.html', context=context)


def message(request):
    if request.method == "POST" and request.is_ajax:
        data = json.loads(request.body)
        name = data['form']['name']
        email = data['form']['email']
        subject = data['form']['subject']
        message_ = data['form']['message']
        _message_ = Message.objects.create(name=name, email=email, subject=subject, message=message_)
        _message_.save()
        context = {'Success': 'Message sent'}
        return JsonResponse(context)
