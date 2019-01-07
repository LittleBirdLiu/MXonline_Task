# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from .models import Teacher, CourseOrg, CityDict

from pure_pagination import Paginator, PageNotAnInteger, EmptyPage
from .forms import UserAskForm
from django.http import HttpResponse
from course.models import course
from operation.models import UserFavourite

# Create your views here.
class Org_List_View(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # sorting the course
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
                print('all orgs by students', all_orgs)
            if sort == 'courses':
                all_orgs = all_orgs.order_by('-course_num')
            else:
                all_orgs = all_orgs.order_by('-add_time')
        else:
            all_orgs = all_orgs.order_by('-add_time')
        # page separate
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        orgs_number = all_orgs.count()

        hotest_orgs = all_orgs.order_by('-click_nums')[:3]

        return render(request, 'org-list.html',
                      {'all_orgs': orgs,
                       'all_cities': all_cities,
                       'orgs_number': orgs_number,
                       'city_id': city_id,
                       'category': category,
                       'hotest_orgs': hotest_orgs,
                       'sort': sort}
                      )

    def post(self, request):
        pass


class UserAskView(View):
    # 用户添加咨询
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            # 返回的json 要用双引号
            return HttpResponse('{"status": "success"}',
                                content_type='application/json')
        else:
            return HttpResponse('{"status": "fail",'
                                ' "msg":"提交失败"}',
                                content_type='application/json')

class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 对于所有有外键
        # 判断是否已经收藏
        has_fav = False
        if request.user.is_authenticated():
            if_fav = UserFavourite.objects.filter(user= request.user, fav_id=int(course_org.id), fav_type=2)
            if if_fav:
                has_fav = True
            else:
                has_fav = False
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html',
                       {
                           'all_courses': all_courses,
                           'all_teachers': all_teachers,
                           'org': course_org,
                           'current_page': current_page,
                           'has_fav' : has_fav
                       })




    def post(self, request):
        pass


class OrgDetailView(View):
    def get(self, request, org_id):
        current_page = 'org'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if_fav = UserFavourite.objects.filter(user= request.user, fav_id=int(course_org.id), fav_type=2)
            if if_fav:
                has_fav = True
            else:
                has_fav = False
        return render(request, 'org-detail-desc.html',
                      {
                          'org': course_org,
                          'current_page': current_page,
                          'has_fav': has_fav
                      })


class CourseDetailView(View):
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if_fav = UserFavourite.objects.filter(user= request.user, fav_id=int(course_org.id), fav_type=2)
            if if_fav:
                has_fav = True
            else:
                has_fav = False
        return render(request, 'org-detail-course.html',
                      {
                          'all_courses': all_courses,
                          'org': course_org,
                          'current_page': current_page,
                          'has_fav': has_fav
                      }
                      )


class TeachersDetailView(View):
    def get(self, request, org_id):
        current_page = 'teachers'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if_fav = UserFavourite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=2)
            if if_fav:
                has_fav = True
            else:
                has_fav = False

        return render(request, 'org-detail-teachers.html',
                      {
                          'all_teachers': all_teachers,
                          'org': course_org,
                          'current_page': current_page,
                          'has_fav': has_fav
                      }
                      )


class AddFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', '')
        fav_type = request.POST.get('fav_type', '')

        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "user not login"}', content_type='application/json')
        else:
            exist_record = UserFavourite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
            if exist_record:
                exist_record.delete()
                return HttpResponse('{"status": "success", "msg": "收藏"}', content_type='application/json')
            else:
                user_fav = UserFavourite()
                if int(fav_id) > 0 and int(fav_type) > 0:
                    user_fav.user = request.user
                    user_fav.fav_id = int(fav_id)
                    user_fav.fav_type = int(fav_type)
                    user_fav.save()
                    return HttpResponse('{"status": "success", "msg": "收藏成功"}', content_type='application/json')
                else:
                    return HttpResponse('{"status": "fail", "msg": "收藏失败"}', content_type='application/json')

