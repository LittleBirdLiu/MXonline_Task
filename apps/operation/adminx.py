import xadmin

from .models import UserAsk, CourseCommit, UserFavourite, UserMessage, UserCourse

class UserAskAdmin(object):
	list_display = ['name', 'mobile', 'course_name', 'add_time']
	search_list = ['name', 'mobile', 'course_name']
	list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommitAdmin(object):
	list_display = ['user', 'course', 'commit', 'add_time']
	search_list = ['user', 'course', 'commit']
	list_filter = ['user__nick_name', 'course__name', 'commit', 'add_time']


class UserFavouriteAdmin(object):
	list_display = ['user', 'fav_id', 'fav_type', 'add_time']
	search_list = ['user', 'fav_id', 'fav_type']
	list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
	list_display = ['user', 'message', 'has_read', 'add_time']
	search_list = ['user', 'message', 'has_read']
	list_filter = ['user', 'message', 'has_read', 'add_time']

class UserCourseAdmin(object):
	list_display = ['user', 'course', 'add_time']
	search_list = ['user', 'course', 'add_time']
	list_filter = ['user__nick_name', 'course__name', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseCommit, CourseCommitAdmin)
xadmin.site.register(UserFavourite, UserFavouriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)