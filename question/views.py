from django.shortcuts import render, redirect

# Create your views here.
from course.models import Course
from question.forms import QuestionForm
from question.models import Question


def quest(request):

    question=Question.objects.all()

    context={
        "question":question,

    }

    return render(request,"question.html",context)

def quest_id(request):
    question=Question.objects.all()
    context={
        "question":question,
    }
    return render(request,"question.html",context)


def create_question(request):
    form = QuestionForm()
    if request.method == "POST":
        form =QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_question')
        else:
            context = {
                "error": form.errors
            }
            return render(request, "error_page.html", context)
    else:
        return render(request, "display.html", context={"form": form})


