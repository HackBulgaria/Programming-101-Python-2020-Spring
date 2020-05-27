from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Course


def list(request):
    return render(request, 'courses/list.html', {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/detail.html', {'course': course})


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})
