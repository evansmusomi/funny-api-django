from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path("jokes/", CreateView.as_view(), name="create"),
    path('jokes/<int:pk>/', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
