from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^$',
        TemplateView.as_view(template_name='base.html'),
        name='homepage'
    ),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^/app/', include('apps.app.urls', namespace='app')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url("^404/$", TemplateView.as_view(template_name="404.html")),
        url("^500/$", TemplateView.as_view(template_name="500.html")),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
