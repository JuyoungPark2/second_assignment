from django.contrib import admin
from .models import Blog
# from django_summernote.admin import SummernoteModelAdmin
# from .models import summer_note

# Register your models here.


# class summer_noteAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'


# admin.site.register(summer_note, summer_noteAdmin)
admin.site.register(Blog)
