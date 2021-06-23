from django.urls import path
from .views import HomeView, AboutView, SnackListView, SnackDetailView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
]