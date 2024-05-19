from django.urls import path
from apps.gap.views import *

app_name = 'gap'
urlpatterns = [
    path('', RoomListView.as_view(), name='rooms'),
    path('room/<pk>', RoomDetailView.as_view(), name='room'),
    path('opinion-like/<pk>', LikeOpinionView.as_view(), name='opinion-like'),
    path('comment-like/<pk>', LikeCommentView.as_view(), name='comment-like'),
    path('comments/<pk>', OpinionDetailView.as_view(), name='comments')
]