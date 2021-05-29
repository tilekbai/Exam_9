from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.views.generic import DetailView

from gallery.models import User
# Create your views here.

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    # def get_context_data(self, **kwargs):
    #     photos = self.get_object().photos.all()
    #     paginator = Paginator(photos, self.paginate_related_by, orphans=self.paginate_related_orphans)
    #     page_number = self.request.GET.photosget('page', 1)
    #     page = paginator.get_page(page_number)
    #     kwargs['page_obj'] = page
    #     kwargs['photos'] = page.object_list
    #     kwargs['is_paginated'] = page.has_other_pages()
    #     return super().get_context_data(**kwargs)