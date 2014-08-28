from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'three_most_important_things.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'accounts.views.login_user', name='login'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^today/$', 'polymer.views.today', name='today'),
    url(r'^history/$', 'polymer.views.history', name='history'),
    url(r'^$', 'polymer.views.home', name='home'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)