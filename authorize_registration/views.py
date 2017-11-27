from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_protect


@csrf_protect
def registration_view(request):
    """ Регистрирует и авторизирует """
    if request.method == "POST":
        user_creation_form = UserCreationForm(QueryDict(request.POST.get('form')))
        if user_creation_form.is_valid():
            user_creation_form.save()
            new_user = auth.authenticate(username=user_creation_form.cleaned_data['username'],
                                         password=user_creation_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return JsonResponse({'answer': 'ok', 'url_redirect': reverse('message:message')})
        else:
            return JsonResponse(
                {'answer': 'bad', 'errors': 'Проверьте форму на правильность заполнения'})
    return render(request, 'authorize_registration/registration.html', {'form': UserCreationForm()})


@csrf_protect
def authorize_view(request):
    """ Авторизация пользователя """
    if request.method == 'POST':
        get_authorize_form = QueryDict(request.POST.get('form'))
        username = get_authorize_form.get('username')
        password = get_authorize_form.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'answer': 'ok', 'url_redirect': reverse('message:message')})
        else:
            return JsonResponse({'answer': 'bad', 'errors': 'Не верный  логин или пароль'})
    else:
        return render(request, 'authorize_registration/authorize.html', {})
