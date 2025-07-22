from django.shortcuts import render, redirect
from django.views.generic import View
from .models import User, Project, Music

# Create your views here.


class HomeView(View):
    def get(self, request):
        project = Project.objects.all()
        
        return render(request, 'home.html', {'project': project})

class ProjectDetailView(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        
        return render(request, 'project_detail.html', {'project': project})

class AboutView(View):
    def get(self, request):
        music = Music.objects.all()
        
        return render(request, 'about.html', {'music': music})
    
class ProjectsView(View):
    def get(self, request):
        search = request.GET.get('search', '')
        
        projects = Project.objects.all()
        if search:
            projects = projects.filter(name__icontains=search)
        
        # AJAX запрос - возвращаем только фрагмент
        if request.headers.get('HX-Request'):
            return render(request, 'fragments/project_cards.html', {
                'projects': projects,
                'search': search
            })
        
        return render(request, 'projects.html', {
            'projects': projects,
            'search': search
        })

class ContactsView(View):
    def get(self, request):
        return render(request, 'contacts.html')

class SkillsView(View):
    def get(self, request):
        return render(request, 'skills.html')



class GithubView(View):
    def get(self, request):
        return redirect('https://github.com/testMonzeN/PhantomTestWeb/tree/host')

class BlogGithubView(View):
    def get(self, request):
        return redirect('https://github.com/testMonzeN/myfirstblog')