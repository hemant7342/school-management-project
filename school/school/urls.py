from django.contrib import admin
from django.urls import path
from api.views import RegisterView,login_view,principal_dashboard,teacher_dashboard,student_dashboard,default_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RegisterView.as_view(), name='register'),
    path("login/", login_view, name="login"),
    path("principal/", principal_dashboard, name="principal_dashboard"),
    path("teacher/", teacher_dashboard, name="teacher_dashboard"),
    path("student/", student_dashboard, name="student_dashboard"),
    path("dashboard/", default_dashboard, name="default_dashboard"),
]

