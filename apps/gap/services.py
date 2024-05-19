from .models import Room, Opinion, Comment, CommentLike
from django.db.models import Model


def model_objects_all(model:Model):
    return model.objects.all()

def model_objects_get_pk(model:Model, pk):
    return model.objects.get(pk=pk)

