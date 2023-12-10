from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render

from .controllers import ParkingSpaceController
from .models import ParkingSpace


class AdminInterface(TemplateView):
    def __init__(self, **kwargs: Any) -> None:
        self.parking_space_controller = ParkingSpaceController()
        super().__init__(**kwargs)

    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.id is None:
            return render(request, '/home/konstantin/bsuir/omix/lab2/django/parking/templates/main/main.html',
                          {'pk': request.user.id})
        if 'delete' in request.path:
            self.parking_space_controller.delete_parking_space(id=request.path.split('/')[-2])
            return redirect('admin', pk=request.user.id)
        if 'update' in request.path and request.method.lower() == 'post':
            row_id, error = self.parking_space_controller.change_parking_space(request=request,
                                                                               id=request.path.split('/')[-2])
            if row_id:
                return redirect('admin', pk=request.user.id)
            else:
                return self.detail(request, error=error)
        if 'detail' in request.path and request.method.lower() == 'get':
            return self.detail(request)
        elif 'create' in request.path and request.method.lower() == 'get':
            return self.create(request)
        elif 'create' in request.path and request.method.lower() == 'post':
            row_id, error = self.parking_space_controller.add_parking_space(request=request)
            if row_id:
                return redirect('admin', pk=request.user.id)
            else:
                return self.create(request, error)
        elif 'place' in request.path and request.method.lower() == 'get':
            return self.history(request)
        elif 'admin' in request.path:
            return self.main(request)
        return super().dispatch(request, *args, **kwargs)

    def main(self, request):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/adminmain/main.html'
        return super().get(request)

    def create(self, request, error=False):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/createplace/main.html'
        context = self.get_context_data()
        if error:
            context['error'] = error
        return self.render_to_response(context)

    def history(self, request):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/showplaces/main.html'
        context = self.get_context_data()
        context['orders'] = []
        queryset = ParkingSpace.objects.filter()
        for i in enumerate(queryset):
            context['orders'].append((i[0] + 1, i[1].id, i[1].status))
        return self.render_to_response(context)

    def detail(self, request, error=False):
        self.template_name = '/home/konstantin/bsuir/omix/lab2/django/parking/templates/showplacesdetail/main.html'
        context = self.get_context_data()
        context['order'] = ParkingSpace.objects.filter(id=request.path.split('/')[-2])[0]
        context['order_id'] = request.path.split('/')[-2]
        if error:
            context['error'] = error
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.request.user.id
        return context
