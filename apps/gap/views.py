from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from apps.gap.models import Room, Opinion, CommentLike,OpinionLike
from .services import *

class RoomListView(View):
   
    def get(self, request):
        context = {}
        context['rooms'] = model_objects_all(Room)
        return render(request, "gap/rooms.html",context=context)

class RoomDetailView(View):

    def get(self, request, pk):
        context = {}
        room = Room.objects.get(pk=pk)

        opinions = sorted(Opinion.objects.filter(room=room), key=lambda o: o.like_count, reverse=True)
        context['room'] = room
        context['opinions'] = opinions
        return render(request, "gap/opinions.html", context=context)
    

class LikeOpinionView(View):

    def get(self, request, pk):
        opinion = model_objects_get_pk(Opinion, pk)
        like, created = OpinionLike.objects.get_or_create(likes=request.user, opinion=opinion)
        if not created: like.delete()
        return redirect(reverse("gap:room", kwargs={"pk": opinion.room.pk}))

class LikeCommentView(View):
    def get(self, request, pk):
        comment = model_objects_get_pk(Comment, pk)
        like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)
        if not created:
            like.delete()
        return redirect(reverse("gap:room", kwargs={"pk":comment.pk}))
        
class OpinionDetailView(View):
    
    def get(self, request, pk):
        context = {}
        opinion = model_objects_get_pk(Opinion, pk)
        comments = opinion.comments.all().order_by("-created_at")
        context['opinion'] = opinion
        context['comments'] = comments
        return render(request, "gap/comments.html", context=context)
    
