from django.urls import path

# from .models import Question
# from django.contrib.sitemaps import GenericSitemap
# from django.contrib.sitemaps.views import sitemap

from . import views

# polls_dict = { 
#     'queryset':Question.objects.all(),
#     'date_field':'pub_date', 
#     }

# sitemaps = {
#     'polls': GenericSitemap(polls_dict, priority=0.6)
#     }



app_name = 'login'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('confirm/', views.confirm, name='confirm'),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('signal/', views.send_signal, name='send_signal'),
    # path('messages/', views.send_messages, name='send_messages'),
    # path('paginator/', views.paginator_result, name='paginator_result'),
    # path('paginatorView/', views.paginatorView.as_view(), name="paginator_result_view"),
    # path('send_a_mail/', views.send_a_mail, name='send_a_mail'),
]