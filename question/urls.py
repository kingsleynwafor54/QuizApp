from django.urls import path

from question import views

urlpatterns=[
    path("",views.quest),
     path("1/",views.quest_id),
    path("question/",views.create_question,name="create_question"),
]