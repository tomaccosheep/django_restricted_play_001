from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Play_Project
import json
import os 
import subprocess
import fileinput
import time


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

def save(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    saved = False
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        proj.con_001 = json_data['con_001']
        proj.save()
        saved = True
    return JsonResponse({'saved': saved})


def make(request, project_id):
    dir_path = os.path.dirname(os.path.realpath(__file__))    
    template_string = dir_path + "/django_template_dir/user_project"
    usr_dir_string = dir_path + "/django_usr_dirs/" + project_id
    command_remove = "rm -r {usr_dir}".format(usr_dir = usr_dir_string)
    command_rsync = "rsync -avP {template} {usr_dir}".format(template = template_string, usr_dir = usr_dir_string)
#    subprocess.run(command_remove.split(), shell=False)
    subprocess.run(command_rsync.split(), shell=False)
    print("rsync -avP " + template_string + " " + usr_dir_string)
    proj = Play_Project.objects.get(unique_id=project_id)
    print(proj.con_001)
    time.sleep(1)
    for line in fileinput.input([dir_path + "/django_usr_dirs/" + project_id + "/user_project/static/css/style.css"], inplace=True):
        print(line.replace('__con_001__', proj.con_001), end='')
    return JsonResponse({'made': True})
    

def get_site(request):
    return None
