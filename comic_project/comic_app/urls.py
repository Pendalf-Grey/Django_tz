from django.urls import path

from .views import RatingCreateView, ComicRatingView

urlpatterns = [
    path('api/ratings/', RatingCreateView.as_view(), name='rating-create'),
    path('api/comic/<int:id>/rating/', ComicRatingView.as_view(), name='comic-rating'),
]
