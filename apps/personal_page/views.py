import json
import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from apps.personal_page import models


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
