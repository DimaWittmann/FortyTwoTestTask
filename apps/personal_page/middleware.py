from apps.personal_page import models


class RequestLoggerMiddleware(object):

    @staticmethod
    def process_request(request):

        if not request.is_ajax():  # ajax requests spam logger
            log = models.RequestLog(
                path=request.path,
                get=str(dict(request.GET)),
                post=str(dict(request.POST)),
                body=request.body,
                method=request.method,
                encoding=request.encoding
            )
            log.save()

        return None
