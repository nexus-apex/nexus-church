from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('churchmembers/', views.churchmember_list, name='churchmember_list'),
    path('churchmembers/create/', views.churchmember_create, name='churchmember_create'),
    path('churchmembers/<int:pk>/edit/', views.churchmember_edit, name='churchmember_edit'),
    path('churchmembers/<int:pk>/delete/', views.churchmember_delete, name='churchmember_delete'),
    path('churchevents/', views.churchevent_list, name='churchevent_list'),
    path('churchevents/create/', views.churchevent_create, name='churchevent_create'),
    path('churchevents/<int:pk>/edit/', views.churchevent_edit, name='churchevent_edit'),
    path('churchevents/<int:pk>/delete/', views.churchevent_delete, name='churchevent_delete'),
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/create/', views.donation_create, name='donation_create'),
    path('donations/<int:pk>/edit/', views.donation_edit, name='donation_edit'),
    path('donations/<int:pk>/delete/', views.donation_delete, name='donation_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
