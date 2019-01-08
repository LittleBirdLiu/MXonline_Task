from django.shortcuts import render
from django.views.generic.base import View
from .models import course


# Create your views here.
class CourseListView(View):
    def get(self, request):
        all_course = course.objects.all()
        fav_course = all_course.order_by('-fav_numbers')[:2]
        return render(request, 'course-list.html', {
            'all_course': all_course,
            'fav_course': fav_course
        })

    def post(self, request):
        pass


class CourseDetailView(View):
    def get(self, request, course_id):
        course_info = course.objects.filter(id=course_id)[0]
        course_org = course_info.courseOrg
        teacher_num = course_org.teacher_set.all().count()
        return render(request, 'course-detail.html', {
            'course_info': course_info,
            'course_org': course_org,
            'teacher_num': teacher_num
        })
