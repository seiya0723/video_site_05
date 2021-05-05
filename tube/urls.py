from django.urls import path
from . import views


app_name = "tube"
urlpatterns =[
    path('', views.index, name="index"),

    # TIPS:<型:変数名>とすることでビューに変数を与えることができる
    #idをuuidにするので、intをuuidに変える。

    path('delete/<uuid:video_pk>/', views.delete, name="delete"),
    path('update/<uuid:video_pk>/', views.update, name="update"),
    path('single/<uuid:video_pk>/', views.single, name="single"),
    ]
