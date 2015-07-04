import json
import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers


from apps.personal_page import models


def personal_page(request):

    try:
        personal_data = models.Person.objects.get(id=1)
        return render(request, 'personal_page/personal_page.html',
                      {'personal_data': personal_data})
    except ObjectDoesNotExist:
        raise Http404


def show_requests(request):
    logs = models.RequestLog.objects.all()[:10]
    return render(request, 'personal_page/logs.html')


def get_new_request(request):
    if 'last_log' in request.GET:
        last_log = datetime.datetime.strptime(request.GET['last_log'],
                                              '%Y-%m-%dT%H:%M:%S.%f 00:00')
        logs=models.RequestLog.objects.exclude(timestamp__lte=last_log
                                               ).all()[:10]
    else:
        logs=models.RequestLog.objects.all()[:10]

    response_data = []
    for log in logs:
        response_data.append({
            'path': log.path,
            'method': log.method,
            'get': log.get,
            'post': log.post,
            'timestamp': log.timestamp.isoformat(),
        })

    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
