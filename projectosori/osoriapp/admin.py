from django.contrib import admin
from .models import Post
from .models import FashionPost
from .models import FashionComment

admin.site.register(Post)
admin.site.register(FashionPost)
admin.site.register(FashionComment)
