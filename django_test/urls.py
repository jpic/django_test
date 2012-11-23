from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

from .views import SignupView


urlpatterns = patterns("",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^autocomplete_light/", include("autocomplete_light.urls")),
    url(r"^test_app/", include("test_app.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
