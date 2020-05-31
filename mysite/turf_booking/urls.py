from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('/create_turf', views.create_turf, name="index"),
    path('index/<str:pk>/', views.create_slot, name="set_slot"),
    path('user', views.create_user, name="set_user"),
    path('user_login', views.user_login, name="user_login"),
    path('listings/<str:pk>/', views.listings, name="listings"),
    path('listings/<str:upk>/<str:tpk>', views.new_slot, name="new_slot"),
    path('turf_detail/<str:pk>', views.turf_detail, name="turf_detail"),
    path('login_turf', views.login_turf, name="turf_login"),
    path('signup_turf', views.create_turf, name="set_turf"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
