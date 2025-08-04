import os.path

from django.core.management.base import BaseCommand
from blog.models import Post
from django.core.files import File
from pathlib import Path

from fishgramm.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'Add Products and Categories to database'

    def handle(self, *args, **kwargs):
        for post in Post.objects.all():
            if post.preview:
                post.preview.delete(save=False)
        Post.objects.all().delete()

        base_path = Path.joinpath(MEDIA_ROOT, 'contents', 'image')

        posts = [{'title': "Добро пожаловать",
                'text': "Приветствую всех вас в нашем новом приложении с функциональностью блога",
                'filename': "fish1.png",
                'is_public': True,
                'views_counter': 99 },

                 {'title': "Не для публикации",
                  'text': "Если ты это видишь, то я где то проебался",
                  'filename': "fish2.png",
                  'is_public': False,
                  'views_counter': 0}
                 ]
        for post_data in posts:
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'text': post_data['text'],
                    'is_public': post_data['is_public'],
                    'views_counter': post_data['views_counter']
                }

            )
            path_to_img =Path.joinpath(base_path, post_data['filename'])
            with open(path_to_img, 'rb') as f:
                img_file = File(f)
                if post.preview:
                    post.preview.delete(save=False)
                    post.preview.save(os.path.basename(path_to_img), img_file, save=True)
                else:
                    post.preview.save(os.path.basename(path_to_img), img_file, save=True)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {post.title}'))

