from django.shortcuts import render
from django.views.generic.base import View
from .models import course
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
class CourseListView(View):
    def get(self, request):
        all_course = course.objects.all()
        fav_course = all_course.order_by('-fav_numbers')[:2]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # sort page
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_course = all_course.order_by('-fav_numbers')
                print('all orgs by students', all_course)
            if sort == 'students':
                all_course = all_course.order_by('-students')
        else:
            all_course = all_course.order_by('-add_time')
        # page seprate
        p = Paginator(all_course, 5, request=request)
        courses_by_page = p.page(page)
        course_number = all_course.count()

        return render(request, 'course-list.html', {
            'all_course': courses_by_page,
            'fav_course': fav_course,
            'course_number': course_number,
            'sort': sort
        })

    def post(self, request):
        pass


class CourseDetailView(View):
    def get(self, request, course_id):
        course_info = course.objects.filter(id=course_id)[0]
        tag = course_info.tag
        print('what tag is ', tag)
        course_org = course_info.courseOrg
        teacher_num = course_org.teacher_set.all().count()
        all_related_courses = course.objects.filter(tag=tag)[:1]
        print('all related courses %s' % all_related_courses)
        return render(request, 'course-detail.html', {
            'course_info': course_info,
            'course_org': course_org,
            'teacher_num': teacher_num,
            'related_courses': all_related_courses
        })
