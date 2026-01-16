from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.hero_page, name='hero'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
