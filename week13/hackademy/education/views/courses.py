from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django import forms

from education.models import Course


def list(request):
    return render(request, 'courses/list.html', {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/detail.html', {'course': course})


class CrouseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'start_date', 'end_date')


def session(request):
    if not request.session.get('counter'):
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    return render(request, 'courses/session.html')


def new_experiment(request):
    if request.method == "POST":
        data = request.POST
        form = CrouseForm(data=data)
        if form.is_valid():
            new_course = form.save()
            return redirect(reverse('education:courses:list'))
        else:
            return render(request, 'courses/new_experiment.html', {'form': form})
    else:
        form = CrouseForm()
        return render(request, 'courses/new_experiment.html', {'form': form})


def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = CrouseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(reverse('education:courses:list'))
        else:
            return render(request, 'courses/edit_course.html', {'course': course, 'form': form})
    else:
        form = CrouseForm(instance=course)
        return render(request, 'courses/edit_course.html', {'course': course, 'form': form})


def delete_course(request, course_id):
    if request.method == 'POST':
        Course.objects.get(id=course_id).delete()
    return redirect(reverse('education:courses:list'))


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})
