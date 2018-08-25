from django.conf.urls import url
from user import views
urlpatterns = [
    url(r'^login/$',views.user_login.as_view()),
    url(r'^register/$', views.user_register.as_view()),
    url(r'^logout/$',views.user_logout)

]