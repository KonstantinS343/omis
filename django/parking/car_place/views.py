from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render

from .controllers import AuthorizationController, ReservationController
from .models import ParkingSpace


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
        username, error = self.authorization_controller.register(request=request)
        if username:
            return redirect('login')
        else:
            return render(request, self.template_name, {'error': error})


class LoginInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.authorization_controller = AuthorizationController()
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/login/main.html'
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/login/main.html'
        user_id, error = self.authorization_controller.login(request=request)
        if user_id:
            if not request.user.is_superuser:
                return redirect('user', pk=user_id)
            else:
                return redirect('admin', pk=user_id)
        else:
            return render(request, self.template_name, {'error': error})


class UserInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.reservation_controller = ReservationController()
        super().__init__(**kwargs)

    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.id is None:
            return redirect('home')
        if 'delete' in request.path:
            self.reservation_controller.delete_reservation(id=request.path.split('/')[-2], user_id=request.user.id)
            return redirect('user', pk=request.user.id)
        if 'update' in request.path and request.method.lower() == 'post':
            row_id, error = self.reservation_controller.change_reservation(request=request)
            if row_id:
                return redirect('user', pk=request.user.id)
            else:
                return self.detail(request, error=error)
        if 'detail' in request.path and request.method.lower() == 'get':
            return self.detail(request)
        elif 'create' in request.path and request.method.lower() == 'get':
            return self.create(request)
        elif 'create' in request.path and request.method.lower() == 'post':
            row_id, error = self.reservation_controller.add_reservation(request=request)
            if row_id:
                return redirect('user', pk=request.user.id)
            else:
                return self.create(request, error)
        elif 'history' in request.path and request.method.lower() == 'get':
            return self.history(request)
        elif 'user' in request.path:
            return self.main(request)
        return super().dispatch(request, *args, **kwargs)

    def main(self, request):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/usermain/main.html'
        return super().get(request)

    def create(self, request, error=False):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/createres/main.html'
        context = self.get_context_data()
        if error:
            context['error'] = error
        return self.render_to_response(context)

    def history(self, request):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/historyres/main.html'
        context = self.get_context_data()
        context['orders'] = []
        queryset = ParkingSpace.objects.filter(user_id=request.user.id)
        for i in enumerate(queryset):
            context['orders'].append((i[0] + 1, i[1].id))
        return self.render_to_response(context)

    def detail(self, request, error=False):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/historydetailres/main.html'
        context = self.get_context_data()
        context['order'] = ParkingSpace.objects.filter(user_id=request.user.id, id=request.path.split('/')[-2])[0]
        context['order_id'] = request.path.split('/')[-2]
        if error:
            context['error'] = error
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.request.user.id
        return context
