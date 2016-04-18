from django.conf.urls import include, url
from django.contrib import admin
import app.views
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'summarizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home_view'),
	url(r'^app/$', 'app.views.landing_view'),

]
