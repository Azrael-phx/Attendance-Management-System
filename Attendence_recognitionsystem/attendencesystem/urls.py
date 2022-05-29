from django import views
from django.urls import URLPattern, path
from .views import *
from django.views.generic import RedirectView

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
urlpatterns = [
    path('',homePageView),
    path('Contact/',contactPageView),
    path('Login/',loginPageView),
    path('About/',aboutPageView),
    path('Home/',create_dataset),
    path('Processing/',preprocessing),
    path('Train/',Training),
    path('Recognition/',recognize),

]

