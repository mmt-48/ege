from django.contrib import admin
from .models import Probl
from .models import Topic
from .models import Exam
from .models import Bimg
from .models import Themes

# Register your models here.
admin.site.register(Probl)
admin.site.register(Topic)
admin.site.register(Exam)
admin.site.register(Bimg)
admin.site.register(Themes)