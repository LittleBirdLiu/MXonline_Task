import xadmin
from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
	list_display = ['name', 'desc', 'add_time']
	search_fields = ['name', 'desc']
	list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
	list_display = ['name', 'desc', 'num_class', 'num_fav', 'image', 'city', 'add_time']
	search_fields = ['name', 'desc', 'num_class', 'num_fav', 'image', 'city']
	list_filter = ['name', 'desc', 'num_class', 'num_fav', 'image', 'city__name', 'add_time']


class TeacherAdmin(object):
	list_display = ['name', 'desc', 'work_year', 'work_company', 'work_position', 'points']
	search_fields = ['name', 'desc', 'work_year', 'work_company', 'work_position', 'points']
	list_filter = ['name', 'desc', 'work_year', 'work_company', 'work_position', 'points']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

