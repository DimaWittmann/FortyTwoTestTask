from django.conf.urls import patterns, url
from fortytwo_test_task.settings import common
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'personal_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'personal_page.views.personal_page', name='personal_page'),
    url(r'^edit_page$', 'personal_page.views.edit_page', name='edit_page'),
    url(r'^requests$', 'personal_page.views.show_requests', name='requests'),

    url(r'^api/new_requests', 'personal_page.views.get_new_request',
        name='new_requests'),
    url(r'^api/personal_data', 'personal_page.views.personal_data',
        name='personal_data'),
) + static(common.MEDIA_URL, document_root=common.MEDIA_ROOT)
