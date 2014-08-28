import json
from datetime import date
from django.shortcuts import render, render_to_response, RequestContext, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from polymer.models import Day, Task


@login_required(login_url='/login/')
def home(request):
    return render_to_response('index.html', {}, RequestContext(request))


@login_required(login_url='/login/')
@csrf_exempt
def today(request):
    today = date.today()
    if request.method == "POST" and request.body.decode('utf-8'):
        print request.body.decode('utf-8')
        day, created = Day.objects.get_or_create(account=request.user, date=today)
        for i, task in enumerate(json.loads(request.body.decode('utf-8'))):
            print i, task
            t, created = Task.objects.get_or_create(day=day, priority=i + 1)
            t.title = task['title']
            t.completed = task['completed']
            t.save()
        return HttpResponse(status=200, content_type='application/json',
                            content=render(request, 'tasks.json', {'tasks': day.task_set.all()}))
    else:
        day, created = Day.objects.get_or_create(account=request.user, date=today)
        return HttpResponse(status=200, content_type='application/json',
                            content=render(request, 'tasks.json', {'tasks': day.task_set.all()}))