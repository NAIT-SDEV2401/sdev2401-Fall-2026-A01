from django.urls import path
from .views import AnnouncementListView, create_announcement

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('create/', create_announcement, name='create_announcement'),
]
