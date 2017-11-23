from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.views import generic

from message.forms import MessageForm
from message.models import Message


def logout(request):
    auth.logout(request)
    return redirect('authorize_registration:authorize')


def send_message_return_status(message):
    """
    отправляет сообщение на эл. почту, возвращает статус отправки
    """
    mail = EmailMessage(message.title_text, message.text, message.parent_username,
                        [message.recipient_email])

    if mail.send(fail_silently=False):
        return Message.SENT
    else:
        return Message.NOT_SENT


class MessageCreate(LoginRequiredMixin, generic.CreateView):
    """
    Отображает форму отправки, сохраняет сообщение в базу отправляет сообщение
    """
    form_class = MessageForm
    template_name = 'message/message.html'
    success_url = '/message/'

    def dispatch(self, request, *args, **kwargs):
        """
        Допишет в self текущего пользователя
        """
        self.user = request.user
        return super(MessageCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        заполняем недостоющие поля, вызавет send_message_return_status()
        """

        message = form.save(commit=False)
        message.parent_username = self.user
        message.status = send_message_return_status(message)
        message.save()
        return super(MessageCreate, self).form_valid(form)


