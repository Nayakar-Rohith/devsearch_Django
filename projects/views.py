from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects=Project.objects.all()
    data={'projects':projects}
    return render(request,'projects/projects.html',data)

def project(request,kp):
    project=Project.objects.get(id=kp)
    return render(request,'projects/single-project.html',{'project':project})

def createProject(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project_forms.html',context)

def updateProject(request,kp):
    project=Project.objects.get(id=kp)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project_forms.html',context)

def deleteProject(request,kp):
    project=Project.objects.get(id=kp)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'projects/delete_template.html',context)



