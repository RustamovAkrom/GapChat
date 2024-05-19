from apps.users.models import User
from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE

class AbstractModel(Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
#p

class Room(AbstractModel):
    name = CharField(max_length=42)

    def __str__(self):
        return self.name


class Opinion(AbstractModel):
    room = ForeignKey(Room, CASCADE, 'opinions')
    title = CharField(max_length=256)
    body = TextField()
    author = ForeignKey(User, CASCADE, 'opinions')

    @property
    def like_count(self):
        return self.author.opinions.count()

    def __str__(self):
        return self.title


class OpinionLike(AbstractModel):
    user = ForeignKey(User, CASCADE, 'likes')
    opinion = ForeignKey(Opinion, CASCADE, 'opinions')

    def __str__(self):
        return f"{self.opinion}-{self.user}"



class Comment(AbstractModel):
    body = TextField()
    opinion = ForeignKey(Opinion, CASCADE, 'comments')
    author = ForeignKey(User, CASCADE, 'comments')

    @property
    def like_count(self):
        return self.opinion.likes.count()

    def __str__(self):
        return self.body
    
class CommentLike(AbstractModel):
    user = ForeignKey(User, CASCADE, 'users')
    comment = ForeignKey(Comment, CASCADE, 'comments')

    def __str__(self):
        return f"{self.comment}-{self.user}"
