import json
import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

from apps.personal_page import models
from apps.personal_page.forms import PersonForm


def personal_page(request):

    try:
        personal_data = models.Person.objects.get(id=1)
        return render(request, 'personal_page/personal_page.html',
                      {'personal_data': personal_data})
    except ObjectDoesNotExist:
        raise Http404


def show_requests(request):
    return render(request, 'personal_page/logs.html')


def get_new_request(request):
    if 'last_log' in request.GET:
        last_log = datetime.datetime.strptime(request.GET['last_log'],
                                              '%Y-%m-%dT%H:%M:%S.%f 00:00')
        logs = models.RequestLog.objects.exclude(
            timestamp__lte=last_log).all()[:10]
    else:
        logs = models.RequestLog.objects.all()[:10]

    response_data = []
    for log in logs:
        response_data.append({
            'path': log.path,
            'method': log.method,
            'get': log.get,
            'post': log.post,
            'timestamp': log.timestamp.isoformat(),
        })

    not_read_logs = models.RequestLog.objects.filter(read=False).all()
    for log in not_read_logs:
        log.read = True
        log.save()

    response_data = {'logs': response_data, 'new': len(not_read_logs)}

    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")


def edit_page(request):
    init_data = model_to_dict(models.Person.objects.first())
    form = PersonForm(initial=init_data)
    return render(request, 'personal_page/edit_page.html', {'form': form})


def personal_data(request):
    print(request.method)
    if request.method == "POST":
        init_data = model_to_dict(models.Person.objects.first())
        form = PersonForm(request.POST, request.FILES, initial=init_data)

        if form.is_valid():
            print(form.has_changed())
            m = models.Person.objects.first()
            m.image = form.cleaned_data['image']
            m.save()
            return HttpResponse("OK")
        else:
            errors_dict = {}

            if form.errors:
                for error in form.errors:
                    errors_dict[error] = form.errors[error]
            print(errors_dict)

            return HttpResponseBadRequest(json.dumps(errors_dict),
                                          content_type="application/json")
