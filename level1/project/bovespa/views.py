from django.views.generic.base import View
from django.template.response import TemplateResponse
from alpha_vantage.timeseries import TimeSeries
import json
import os

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        ALPHA_VANTAGE_API_KEY = os.environ['ALPHA_VANTAGE_API_KEY']
        ts = TimeSeries(key='ALPHA_VANTAGE_API_KEY')
        data, meta_data = ts.get_weekly(symbol='^BVSP.BS', outputsize='full')
        with open('data.json','w') as f:f.write(json.dumps(data, indent=4))
        with open('meta_data.json','w') as f:f.write(json.dumps(meta_data, indent=4))
        return TemplateResponse(request, self.template_name, {})