from django.urls import path, include
from . import views
# from .views import SignUpView
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path ('',views.index, name = 'index'),
    path ('show/',views.show, name = 'show'),
    path ('add/',views.add, name = 'add'),
    path('showdata/<int:id>',views.showdata, name = 'showdata'),

    # path('signup/', SignUpView.as_view(), name='signup'),
    path ('config/',include('django.contrib.auth.urls')),
    # path ('accounts/',include('gsk.urls')),
    # path ('',TemplateView.as_view(template_name = 'home.html'),name = 'home')
    # path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
urlpatterns += staticfiles_urlpatterns()