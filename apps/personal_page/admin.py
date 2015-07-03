from django.contrib import admin
from apps.personal_page.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'email',
                    'jabber', 'skype')
    list_display_links = ('last_name',)


admin.site.register(Person, PersonAdmin)
