import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'course_num', 'num_fav', 'image', 'city', 'add_time']
    search_fields = ['name', 'desc', 'course_num', 'num_fav', 'image', 'city']
    list_filter = ['name', 'desc', 'course_num', 'num_fav', 'image', 'city__name', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'desc', 'work_year', 'work_company', 'work_position', 'points', 'image']
    search_fields = ['org', 'name', 'desc', 'work_year', 'work_company', 'work_position', 'points', 'image']
    list_filter = ['org','name', 'desc', 'work_year', 'work_company', 'work_position', 'points', 'image']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
