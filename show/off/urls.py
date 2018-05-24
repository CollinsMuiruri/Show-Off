from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.liveshowoffs, name='liveshowoffs'),
    url(r'^home/$', views.welcome, name='welcome'),
    url(r'^detail/(?P<image_id>\d+)', views.detail, name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
