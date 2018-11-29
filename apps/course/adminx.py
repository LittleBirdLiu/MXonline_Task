from .models import CourseResource, Lesson, Video, course

import xadmin
class courseAdmin(object):
	list_display = ['name', 'desc', 'detail', 'degree', 'learn_time',
	                'studtent', 'fav_numbers', 'image', 'click_number',
	                'add_time']
	search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time',
	                 'studtent', 'fav_numbers', 'image', 'click_number',
	                 ]
	list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time',
	               'studtent', 'fav_numbers', 'image', 'click_number',
	               'add_time']

xadmin.site.register(course, courseAdmin)


class LessonAdmin(object):
	list_display = ['course', 'name', 'add_time']
	search_fields = ['course', 'name']
	list_filter = ['course__name', 'name', 'add_time']

xadmin.site.register(Lesson, LessonAdmin)

class VideoAdimin(object):
	list_display = ['lesson', 'name', 'add_time']
	search_fields = ['lesson', 'name']
	list_filter = ['lesson__name', 'name', 'add_time']

xadmin.site.register(Video, VideoAdimin)

class CourseResourceAdmin(object):
	list_display = ['course', 'name','download', 'add_time']
	search_fields = ['course', 'name','download']
	list_filter = ['course__name', 'name','download', 'add_time']

xadmin.site.register(CourseResource, CourseResourceAdmin)
