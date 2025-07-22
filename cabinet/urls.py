from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ProjectDetailView, GithubView, BlogGithubView, ContactsView, SkillsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('skills/', SkillsView.as_view(), name='skills'),

    path('pahntom/', GithubView.as_view(), name='phantom_github'),
    path('blog/', BlogGithubView.as_view(), name='blog_github'),
]