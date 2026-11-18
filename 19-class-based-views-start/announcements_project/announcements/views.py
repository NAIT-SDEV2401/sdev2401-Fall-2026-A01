from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Announcement
from .forms import AnnouncementForm
from django.views import View

@method_decorator(login_required, name='dispatch')
class AnnouncementListView(View):
    template_name='announcements/announcement_list.html'
    def get(self, request):
        announcements = Announcement.objects.all().order_by('-created_at')
        return render(
            request,
            self.template_name,
            {'announcements': announcements}
        )

# our test function here.
def is_teacher(user):
    # the user object is passed in here by the decorator
    return user.role == 'teacher'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_teacher, login_url='login'), name='dispatch')
class CreateAnnouncementView(View):
    template_name = 'announcements/create_announcement.html'
    form_class = AnnouncementForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()
            return redirect('announcement_list')
        return render(request, self.template_name, {'form': form})
    