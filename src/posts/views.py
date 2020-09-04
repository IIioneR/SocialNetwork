import datetime

from django.db.models.aggregates import Count
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.state import User

from posts.models import Like, Post, Profile
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def like(self, request, pk):
        # Create or updates Like object for current user, with value=`True`
        obj, _ = Like.objects.update_or_create(user=request.user, post_id=pk)
        obj.update_is_liked(True)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def unlike(self, request, pk):
        # Create or updates Like objects for current user, with value=`False`
        obj, _ = Like.objects.update_or_create(user=request.user, post_id=pk)
        obj.update_is_liked(False)
        return Response(status=status.HTTP_200_OK)


class Analytics(APIView):

    def get(self, request):
        '''
        Returns analytics for a period from query params:
        :date_from: 'YYYY-mm-dd'
        :date_to: 'YYYY-mm-dd'
        400 in case if incoming date format doesn't match
        '''
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        try:
            datetime.datetime.strptime(date_from, '%Y-%m-%d')
            datetime.datetime.strptime(date_to, '%Y-%m-%d')
        except:
            return Response(data='request must contain following query params(date_from, date_to),'
                                 ' in the following format : 2020-03-05', status=status.HTTP_400_BAD_REQUEST)

        qs = Like.objects.filter(liked_at__range=[date_from, date_to]) \
            .extra({"day": "date_trunc('day', liked_at)"}).values("day").order_by().annotate(Count("id"))
        return Response(data=qs, status=status.HTTP_200_OK)


class Activity(APIView):
    def get(self, request):
        '''
        Returns users activity in the following format:
        {
            "last_login": datetime.datetime,
            "last_request": datetime.datetime,
        }
        '''

        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=request.user)

        return Response(data={"last_login": user.last_login, "last_request": profile.last_request},
                        status=status.HTTP_200_OK)
