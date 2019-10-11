from django.http import HttpResponse

from luminus.managers import course_manager


def get_course(request, code):
    course = course_manager.get_course(code)
    return HttpResponse(str(course), status=200)


def get_course_by_code(request, code):
    course = course_manager.get_course_by_code(code)
    return HttpResponse(str(course), status=200)


def get_course_by_puname(request, puname):
    course = course_manager.get_course_by_puname(puname)
    return HttpResponse(str(course), status=200)


def get_course_by_tuname(request, tuname):
    course = course_manager.get_course_by_tuname(tuname)
    return HttpResponse(str(course), status=200)


def get_course_by_suname(request, suname):
    course = course_manager.get_course_by_suname(suname)
    return HttpResponse(str(course), status=200)