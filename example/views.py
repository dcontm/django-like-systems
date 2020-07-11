from django.views.generic import ListView
from . models import Test

# Create your views


class HomeView(ListView):
    template_name = "home.html"
    context_object_name = "my_list"
    queryset = Test.objects.all()
