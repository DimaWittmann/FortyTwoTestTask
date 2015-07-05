from django.forms.widgets import FileInput

from fortytwo_test_task.settings.common import MEDIA_URL


class ImageWidget(FileInput):

    def render(self, name, value, attrs=None):
        input_field = super(ImageWidget, self).render(name, value, attrs)
        url = MEDIA_URL + str(value)

        html = "<div>"
        html += "<img src=%s alt=%s>" % (url, "Image not found")
        html += input_field
        html += "</div>"
        return html
