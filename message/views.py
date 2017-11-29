from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.views import generic

from message.forms import MessageForm
from message.models import Message


def logout(request):
    auth.logout(request)
    return redirect('auth_app:authorize')


class MessageCreate(LoginRequiredMixin, generic.CreateView):
    """ Отображает форму отправки, сохраняет сообщение в базу отправляет сообщение """
    form_class = MessageForm
    template_name = 'message/message.html'
    success_url = '/message/'

    def dispatch(self, request, *args, **kwargs):
        """ Допишет в self текущего пользователя """
        self.user = User.objects.get(username=request.user)
        return super(MessageCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """ Заполнит недостающие поля, и отправит сообщение на эл. почту """
        message = form.save(commit=False)
        message.parent_username = self.user
        mail = EmailMessage(message.title_text, message.text, self.user.email,
                            [message.recipient_email])
        if mail.send(fail_silently=False):
            message.status = Message.SENT
        else:
            message.status = Message.NOT_SENT
        message.save()
        return super(MessageCreate, self).form_valid(form)
