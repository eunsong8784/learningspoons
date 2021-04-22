from django.urls import path
from . import views
#post_list라는 view가 루트 url에 할당, 누군가 도메인 주소로 들어오면 views.post_list
urlpatterns = [
    path('', views.post_list, name='post_list'),
]