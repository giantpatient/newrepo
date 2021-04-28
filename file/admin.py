from django.contrib import admin
from . models import file,feedback
# Register your models here.

class feedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)


admin.site.register(file)
admin.site.register(feedback,feedbackAdmin)