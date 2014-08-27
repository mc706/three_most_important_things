from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'three_most_important_things.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/$', 'polymer.views.data', name='data'),
    url(r'^$', 'polymer.views.home', name='home'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)