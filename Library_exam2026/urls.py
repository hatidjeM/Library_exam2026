from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Library_exam2026 import views



urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('categories/', include('categories.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])