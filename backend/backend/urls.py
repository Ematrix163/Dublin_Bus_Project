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
from django.urls import path, re_path
from django.conf.urls import handler404, handler500, handler400, handler403

from api.views import RouteIdView, RoutesStopidView, PredictTimeView, DirectionView, LocationView, error_404, error_500, StaticFileView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	re_path('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^login$', TemplateView.as_view(template_name="index.html"), name="index"),
    path('admin/', admin.site.urls),
    path('api/allroutes', RouteIdView.as_view()),
    path('api/station', RoutesStopidView.as_view()),
    path('api/direction',DirectionView.as_view()),
    path('api/time', PredictTimeView.as_view()),
    path('api/googleroute', LocationView.as_view()),
    path('api/static',StaticFileView.as_view())
]

# This is to avoid the conflicts with react router
# urlpatterns += [
#     re_path(r'^.*/', TemplateView.as_view(template_name="index.html"), name='base')
# ]

urlpatterns += staticfiles_urlpatterns()
#
#
# handler404 = error_404
# handler500 = error_500