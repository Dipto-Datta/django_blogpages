from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [    
    path('',views.article_list, name ="list"),
    path('about/',views.aboutPage, name="about"),
    path('details/<slug:slug>/', views.article_detail, name='details'),

]


