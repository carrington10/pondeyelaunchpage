from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.email_list,name="home"),

]