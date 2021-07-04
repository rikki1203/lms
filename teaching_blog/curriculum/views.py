
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView)
from .models import *


# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'
    
class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model= Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    