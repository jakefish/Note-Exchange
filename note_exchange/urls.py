from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

import haystack


admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'', include('social_auth.urls')),
  url(r'^search/', include('haystack.urls'), name="haystack_search"),
  (r'^main/', include('notes_app.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
