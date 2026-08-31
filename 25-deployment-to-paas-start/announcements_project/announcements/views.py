
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# import the mixin we created in the core app
from core.mixins import IsTeacherRoleMixin

# Create your views here.
from .models import Announcement
from .forms import AnnouncementForm

# From the changed to a generic class.
# class AnnouncementListView(LoginRequiredMixin, View):
#     template_name = 'announcements/announcement_list.html'

#     def get(self, request):
#         announcements = Announcement.objects.all().order_by('-created_at')
#         return render(
#             request,
#             self.template_name,
#             {'announcements': announcements}
#         )

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'
    ordering = ['-created_at']


# Change to generic class.
# class CreateAnnouncementView(LoginRequiredMixin, IsTeacherRoleMixin, View):
#     template_name = 'announcements/create_announcement.html'
#     form_class = AnnouncementForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             announcement = form.save(commit=False)
#             announcement.created_by = request.user
#             announcement.save()
#             return redirect('announcement_list')
#         return render(request, self.template_name, {'form': form})

class CreateAnnouncementView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    template_name = 'announcements/create_announcement.html'
    form_class = AnnouncementForm
    success_url = '/announcements/'
    permission_required = 'announcements.add_announcement'

    def form_valid(self, form):
        announcement = form.save(commit=False)
        announcement.created_by = self.request.user
        announcement.save()
        return super().form_valid(form)