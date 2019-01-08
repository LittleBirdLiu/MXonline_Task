from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='list'),
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='detail'),
]
