from django.urls import path

from frontend import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # spath('logout/', views.logout_user, name='logout'),
]