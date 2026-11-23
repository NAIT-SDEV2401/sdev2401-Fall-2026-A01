from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
# import login_required decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

# Create your views here.
from .models import Announcement
from .forms import AnnouncementForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    ordering = ['-created_at']
    context_object_name = 'announcements'
    template_name = 'announcements/announcement_list.html'
    
# this will restrict access to only users that pass the is_teacher test
# it will redirect to the login page if the user does not have permission.
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from core.mixins import IsTeacherRoleMixin 
from django.views.generic import FormView

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