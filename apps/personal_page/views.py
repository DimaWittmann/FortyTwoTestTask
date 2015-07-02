from django.shortcuts import render
from django.http import Http404


from apps.personal_page import models


def personal_page(request):

    if models.Person.objects.count() >= 1:
        personal_data = models.Person.objects.get(id=1)
        return render(request, 'personal_page/personal_page.html', {'personal_data': personal_data})
    else:
        raise Http404
