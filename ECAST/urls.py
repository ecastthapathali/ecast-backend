
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/committee/', include('committee.urls')),
    path('api/event/', include('event.urls')),
    path('api/project/', include('projects.urls')),
    path('api/intake/', include('intake.urls')),
    path('api/article/', include('article.urls')),
    path('api/contact/', include('contact.urls')),
    path('certificates/', include('certificates.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_title = "ECAST Admin Panel"
admin.site.site_header = "ECAST Admin"
