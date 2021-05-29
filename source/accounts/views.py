from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.views.generic import DetailView

from gallery.models import User
# Create your views here.

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'