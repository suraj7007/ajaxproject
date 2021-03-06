from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def home(request):
    data = User.objects.filter()
    context = {'data': data}
    return render(request, 'home.html', context)


def save_data(request):
    if request.method == "POST":
        sid = request.POST.get('stuid')
        nm = request.POST['name']
        em = request.POST['email']
        pw = request.POST['password']
        if sid == '':
            user_data = User(name=nm, email=em, password=pw)
        else:
            user_data = User(id=sid, name=nm, email=em, password=pw)

        user_data.save()
        stud = User.objects.values()
        student_data = list(stud)
        # print(student_data)

        return JsonResponse({'status': "save", 'student_data': student_data})
    else:
        return JsonResponse({'status': 0})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        userid = User.objects.get(id=id)
        userid.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        userid = User.objects.get(id=id)
        student_data = {'id': userid.id, 'name': userid.name,
                        'email': userid.email, 'password': userid.password}
        # return JsonResponse(student_data, {'status':1})
        return JsonResponse(student_data)
    else:
        return JsonResponse({'status': 0})
