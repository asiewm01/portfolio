from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Set the root URL to point to the home view
    path('home/', views.home, name='home'),  # Optional: if you want to keep '/home/' too
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me, name='about_me'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('blog/', views.blog, name='blog'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('tech_stack/', views.tech_stack, name='tech_stack'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
