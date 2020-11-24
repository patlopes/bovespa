from django.views.generic.base import View
from django.template.response import TemplateResponse

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return TemplateResponse(request, self.template_name, {})