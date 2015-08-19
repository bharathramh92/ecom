from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'easy_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.dashboardView, name= "dashboard"),
    url(r'^edit/$', views.editView, name= "edit"),

    url(r'^new/$', views.newView, name= "new"),
    url(r'^new/book/$', views.addNewBookPKCheck, name= "newBookCheck"),
    url(r'^new/book/(?P<isbn>[0-9]*)/$', views.addNewBook, name= "newBook"),
]
