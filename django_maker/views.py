from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Play_Project
import json
import os
import subprocess
import fileinput
import time
from django.utils.crypto import get_random_string

def index(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    context_dict = {'con_001': proj.con_001,
                    'id': proj.id,
                    }
    return render(request, 'django_maker/index.html', context=context_dict)

def new_project(request):
    proj = Play_Project()
    def_id = get_random_string(length=32)
    proj.unique_id = def_id
    proj.save()
    return HttpResponseRedirect('/index/{}/'.format(def_id))

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
    subprocess.run(command_remove, shell=False)
    command_rsync_list = command_rsync.split()
    subprocess.run(command_rsync, shell=False)
    proj = Play_Project.objects.get(unique_id=project_id)
    time.sleep(1)
    for line in fileinput.input([dir_path + "/django_usr_dirs/" + project_id + "/user_project/static/css/style.css"], inplace=True):
        print(line.replace('__con_001__', proj.con_001), end='')
    return JsonResponse({'made': True})

def run(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    usr_dir_string = dir_path + "/django_usr_dirs/" + project_id
    command_run_mig1 = "python3 {usr_dir}/user_project/manage.py makemigrations".format(usr_dir=usr_dir_string)
    command_run_mig2 = "python3 {usr_dir}/user_project/manage.py migrate".format(usr_dir=usr_dir_string)
    command_run_server = "python3 {usr_dir}/user_project/manage.py runserver ".format(usr_dir=usr_dir_string) + str(8000 + proj.id)
    my_env = os.environ.copy()
    my_env["DJANGO_SETTINGS_MODULE"] = "user_project.settings"
#    subprocess.run("printenv", shell=False)
    subprocess.run(command_run_mig1.split(), env=my_env)
    subprocess.run(command_run_mig2.split(), env=my_env)
    subprocess.Popen(command_run_server.split(), env=my_env)
    return JsonResponse({'ran': True})


def view(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    return HttpResponseRedirect('http://127.0.0.1:{}/'.format(str(8000 + proj.id)))

def kill(request, project_id):
    return JsonResponse({'kill': True})
