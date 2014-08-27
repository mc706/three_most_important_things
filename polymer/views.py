from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
import json
# Create your views here.

def home(request):
    return render_to_response('index.html', {}, RequestContext(request))

def data(request):
    demo = [
        {"title": "test1"},
        {"title": "test2"},
        {"title": "test3"}
    ]
    return HttpResponse(status=200, content_type='application/json', content=json.dumps(demo))