from django.contrib import admin

# Register your models here.
from .models import User
from .models import Doctor
from .models import Word
from .models import WordsAttribute
from .models import Appointment
from .models import UserTask
from .models import UserRecording

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Word)
admin.site.register(WordsAttribute)
admin.site.register(Appointment)
admin.site.register(UserTask)
admin.site.register(UserRecording)