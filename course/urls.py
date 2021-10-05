from django.urls import path

from course import views

urlpatterns = [

    path("",views.hello1,name="hello1"),
    path(r'1/',views.hello1,name="hello"),
    path("create/",views.create_course,name="create_course"),
]