from django.urls import path, include
from .views import profile_view, logout, push_detail, push_update, push_delete

urlpatterns = [
    path("profile/", profile_view, name="profile_view"),
    path("logout/", logout, name='logout'),
    path("detail/", push_detail, name='push-detail'),
    path("update/<str:pk>", push_update, name='push-update'),
    path("delete/<str:pk>", push_delete, name='push-delete'),
]
