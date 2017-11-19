from django.contrib import admin


from Event.models import Image_afisha, Event
# Register your models here.

class EventImagesInline(admin.StackedInline):
	model = Image_afisha
	extra = 4

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	inlines = [EventImagesInline]

admin.site.register(Event, EventAdmin)