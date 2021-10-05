from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import CourseForm
from course.models import Course
from question.models import Question


def hello1(request):
    course = Course.objects.all()
    context = {
        "course": course,
    }
    return render(request, "home.html", context)



def create_course(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_course')
        else:
            context = {
                "error": form.errors
            }
            return render(request, "error_page.html", context)
    else:
        return render(request, "update.html", context={"form": form})


