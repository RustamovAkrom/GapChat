


def model_objects_all(model):
    return model.objects.all()

def model_objects_get(model, **kwargs):
    return model.objects.get()

def main():
    comment = Comment.objects.create(body='hellow')
    model_objects_all(comment)

if __name__=='__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    application = get_wsgi_application()
    from apps.gap.models import Room, Opinion, Comment, CommentLike
    from django.db.models import Model
    from apps.gap.models import Room, Comment

    print(main())