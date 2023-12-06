from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


from .controllers import AuthorizationController


class HomeInterface(TemplateView):
    def dispatch(self, request, *args: Any, **kwargs: Any):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/main/main.html'
        return super().dispatch(request, *args, **kwargs)


class RegisterInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.authorization_controller = AuthorizationController()
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/register/main.html'
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/register/main.html'
        self.authorization_controller.register(request=request)
        return redirect('home')


class LoginInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.authorization_controller = AuthorizationController()
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/login/main.html'
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/main/main.html'
        user_id = self.authorization_controller.login(request=request)
        if user_id:
            return redirect('user', pk=user_id)
        else:
            return redirect('home')


class UserInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.authorization_controller = AuthorizationController()
        super().__init__(**kwargs)

    def dispatch(self, request, *args: Any, **kwargs: Any):
        if 'user' in request.path:
            return self.main(request)
        return super().dispatch(request, *args, **kwargs)

    def main(self, request):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/usermain/main.html'
        return super().get(request)
