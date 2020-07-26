from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Test

# Create your views


class HomeView(LoginRequiredMixin, ListView):
    template_name = "home.html"
    context_object_name = "my_list"
    queryset = Test.objects.all()
