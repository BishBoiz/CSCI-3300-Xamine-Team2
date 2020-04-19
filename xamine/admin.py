from django.contrib import admin

from xamine.models import Patient, Level, AppSetting, Order, Image, ModalityOption, Team


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['label', 'image', 'added_on', 'user']
    readonly_fields = ['added_on', 'user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['added_on', 'last_edit']
    inlines = [ImageInline]


admin.site.register(Patient)
admin.site.register(Level)
admin.site.register(AppSetting)
# admin.site.register(Image)
admin.site.register(ModalityOption)
admin.site.register(Team)
