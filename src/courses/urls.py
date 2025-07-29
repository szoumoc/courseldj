from django.urls import path

from . import views

urlpatterns = [
    path("<int:course_id>/lessons/<int:lesson_id>/", views.lesson_detail_view),
    path("<slug:course_id>/", views.course_detail_view),
    path("", views.course_list_view),
]
