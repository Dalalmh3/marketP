from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^Add_Product$', views.Add_Product),
    url(r'^All_Product$', views.All_Products),
    url(r'signup/', views.signup),
    url(r'login/', views.login),
    url(r'logout', views.logout),
]