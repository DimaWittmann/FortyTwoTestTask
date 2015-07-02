from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'personal_page.views.personal_page', name='personal_page'),

)
