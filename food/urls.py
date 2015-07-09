from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from recipes import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(?P<recipe_id>\d+)$', views.view_recipe, name='view_recipe')
]
urlpatterns = patterns('',
    # ... the rest of your URLconf goes here ...
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(?P<recipe_id>\d+)$', views.view_recipe, name='view_recipe'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
