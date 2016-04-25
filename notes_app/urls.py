from django.conf.urls import patterns, url
from notes_app import views
from models import Course, Document

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^thank_you/$', views.thank_you, name='thank_you'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^course/$', views.course_form, name='course'),
    url(r'^get/(?P<document_id>\d+)/$',views.document, name='document'),
    url(r'^doc_form/$', views.doc_form, name = "doc_form"),
    url(r'^more_info/$', views.more_info, name="more_info")
)
