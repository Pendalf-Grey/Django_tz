from rest_framework import generics
from .models import Rating, Comic
from .serializers import RatingSerializer, ComicSerializer


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        comic_id = self.request.data.get('comic_id')
        user_id = self.request.data.get('user_id')
        value = self.request.data.get('value')
        rating_instance, created = Rating.objects.get_or_create(
            comic_id=comic_id,
            user_id=user_id,
            defaults={'value': value}
        )
        if not created:
            rating_instance.value = value
            rating_instance.save()

        comic = Comic.objects.get(id=comic_id)
        ratings = comic.ratings.values_list('value', flat=True)
        average_rating = sum(ratings) / len(ratings)
        comic.rating = average_rating
        comic.save()


class ComicRatingView(generics.RetrieveAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    lookup_field = 'id'

