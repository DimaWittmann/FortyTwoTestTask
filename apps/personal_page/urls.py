from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'personal_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'personal_page.views.personal_page', name='personal_page'),
    url(r'^requests$', 'personal_page.views.show_requests', name='requests'),

    url(r'^api/new_requests', 'personal_page.views.get_new_request',
        name='new_requests'),
)
