import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from snippets.models import Snippet, Tag

class Command(BaseCommand):
    help = 'Insert dummy users and snippets.'

    def add_arguments(self, parser):
        parser.add_argument('--snippets', nargs='?', type=int, default=10)

    def handle(self, *args, **options):
        snippet_count = options.get("snippets")
        for i in range(0,snippet_count):
            import_string = "Hello, World! No:" + str(i) 
            import_code = "print(\'" + import_string + "\')"
            snippet=Snippet(
                title='タイトル' + str(i),
                code= import_code,
                description='こんにちは、世界',
                created_by=User.objects.get(id=1))
            snippet.save()
            # タグの追加
            if i % 4 == 0:
                snippet.tag.add(Tag.objects.get(id=1))
            elif i % 4 == 1:
                snippet.tag.add(Tag.objects.get(id=2))
            elif i % 4 == 2:
                snippet.tag.add(Tag.objects.get(id=1))
                snippet.tag.add(Tag.objects.get(id=2))
            else:
                pass
