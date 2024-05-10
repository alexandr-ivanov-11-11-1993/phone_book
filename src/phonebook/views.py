from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from . import forms
from . import models
import phonebook

class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneFrom
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()