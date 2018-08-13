"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import handler404, handler500, handler400, handler403

from api.views import RouteIdView, RoutesStopidView, PredictTimeView, DirectionView, LocationView, \
    error_404, error_500, StaticFileView, UserPlaceView, SavePlaceView, SignUpView, DeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
	re_path('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^login$', TemplateView.as_view(template_name="index.html"), name="index"),
    path('admin/', admin.site.urls),
    path('api/allroutes', RouteIdView.as_view()),
    path('api/station', RoutesStopidView.as_view()),
    path('api/direction',DirectionView.as_view()),
    path('api/time', PredictTimeView.as_view()),
    path('api/googleroute', LocationView.as_view()),
    path('api/static',StaticFileView.as_view()),
    re_path(r'^api/login$', obtain_jwt_token),
    re_path(r'^api/userdata$', UserPlaceView.as_view()),
    re_path(r'^api/savedata$', SavePlaceView.as_view()),
    re_path(r'^api/signup$', SignUpView.as_view()),
    re_path(r'^api/deletejourney$', DeleteView.as_view())
]

urlpatterns += staticfiles_urlpatterns()


handler404 = error_404
handler500 = error_500