from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Play_Project
def index(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    context_dict = {'con_001': proj.con_001,
                    }
    return render(request, 'django_maker/index.html', context=context_dict)

def new_project(request):
    proj = Play_Project()
    unique_id = proj.unique_id
    proj.save()
    
    return HttpResponseRedirect('/index/{}/'.format(unique_id))

def save(request, proj_id):
    proj = Play_Project.objects.get(unique_id=proj_id)
    saved = False
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        proj.con_001 = json_data['con_001']
        proj.save()
        saved = True
    return JsonResponse({'saved': saved})

def get_site(request):
    return None
