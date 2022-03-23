from django.urls import path
from . import views
# from django.conf.urls import url
# from django.views.decorators.cache import never_cache

urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.compute_results, name='compute_results'),
    path('tweets', views.tweets_pool, name='tweets_pool')
]
