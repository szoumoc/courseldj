from django.shortcuts import render
from django.http import Http404, JsonResponse
from . import services


def course_list_view(request):
    queryset = services.get_publish_courses()
    # return JsonResponse({"data":[x.path for x in queryset]})
    print(queryset)
    context = {
        "object_list":queryset
    }
    
    return render(request, "courses/list.html", context)

def course_detail_view(request,course_id=None,*args, **kwargs):
    course_obj = services.get_course_detail(course_id=course_id)
    print(course_obj)
    if course_obj is None:
       raise Http404
    lessons_queryset = services.get_course_lessons(course_obj)
    context = {
        "object" : course_obj,
        "lessons_queryset" : lessons_queryset,
    }
    # return JsonResponse({"data":course_obj.id,
    #                      "lesson_id":[x.path for x in lessons_queryset]})
    return render(request, "courses/detail.html", context)


def lesson_detail_view(request, lesson_id=None,course_id=None,*args, **kwargs):
    print(course_id,lesson_id)
    lesson_obj = services.get_lesson_detail(course_id=course_id,lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404
    return JsonResponse({"data":lesson_obj.id})
    return render(request, "courses/detail.html", {})