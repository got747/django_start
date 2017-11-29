from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_protect

from auth_app.forms import UserAuthForm, UserCreationCustomForm


@csrf_protect
def registration_view(request):
    """ Регистрирует и авторизирует """
    if request.method == "POST":
        user_creation_form = UserCreationCustomForm(QueryDict(request.POST.get('form')))
        if user_creation_form.is_valid():
            user_creation_form.save()
            new_user = auth.authenticate(username=user_creation_form.cleaned_data['username'],
                                         password=user_creation_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return JsonResponse({'success': True, 'url_redirect': reverse('message:message')})
        else:
            return JsonResponse(
                {'success': False, 'errors': 'Проверьте форму на правильность заполнения или логин занят'})
    return render(request, 'auth_app/registration.html', {'form': UserCreationCustomForm()})


@csrf_protect
def authorize_view(request):
    """ Авторизация пользователя """
    if request.method == 'POST':
        auth_form = UserAuthForm(QueryDict(request.POST.get('form')))
        if auth_form.is_valid():
            user = auth.authenticate(username=auth_form.cleaned_data['username'],
                                     password=auth_form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return JsonResponse({'success': True, 'url_redirect': reverse('message:message')})
            else:
                return JsonResponse({'success': False, 'errors': 'Не верный  логин или пароль'})

    return render(request, 'auth_app/authorize.html', {'form': UserAuthForm()})
