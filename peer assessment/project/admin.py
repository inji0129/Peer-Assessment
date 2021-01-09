from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Poll)
admin.site.register(Peer)
admin.site.register(Comment)
admin.site.register(Score)
