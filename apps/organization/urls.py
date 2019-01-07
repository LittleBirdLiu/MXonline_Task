# _*_ coding : utf-8 _*_

from django.conf.urls import url, include
from .views import Org_List_View, UserAskView, OrgHomeView, OrgDetailView, CourseDetailView, TeachersDetailView, AddFavView

urlpatterns = [
    url(r'^list/$', Org_List_View.as_view(), name='list'),
    url(r'^user-ask/$', UserAskView.as_view(), name='user-ask'),
    url(r'^home/(?P<org_id>\d+)$', OrgHomeView.as_view(), name='org_home'),
    url(r'^org-detail/(?P<org_id>\d+)$', OrgDetailView.as_view(), name='org-detail'),
    url(r'^course-detail/(?P<org_id>\d+)$', CourseDetailView.as_view(), name='course-detail'),
    url(r'^teachers-detail/(?P<org_id>\d+)$', TeachersDetailView.as_view(), name='teachers-detail'),
    url(r'^add_fav/$', AddFavView.as_view(), name='Add-Fav'),
]