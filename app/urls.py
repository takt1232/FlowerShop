from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_page, name='landing_page'),
    path('home', views.landing_page, name='landing_page'),
    path('flower-categories', views.flower_category, name='flower_categories'),
    path('flower-list/<int:pk>/', views.flower_list, name='flower_list'),
    path('flowers/<int:pk>/', views.flower_details, name='flower_details'),
    path('flowers/add/', views.add_flower, name='add_flower'),
    path('flowers/<int:pk>/delete/', views.delete_flower, name='delete_flower'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
