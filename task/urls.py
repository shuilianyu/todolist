from django.conf.urls import url
from task import views
urlpatterns = [
    url(r'^task_list/$',views.task_list.as_view()),
    url(r'^task_detail/(?P<task_id>\d+)/$',views.task_detail.as_view())

]