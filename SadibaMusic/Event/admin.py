from django.contrib import admin


from Event.models import *
#Register your models here.

class EventImagesInline(admin.StackedInline):
	model = Image_portfolio
	extra = 4


class PhoneInline(admin.StackedInline):
	model = Phones
	extra = 2

class VideoInline(admin.StackedInline):
	model = Video
	extra = 2

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	inlines = [EventImagesInline, PhoneInline, VideoInline]

admin.site.register(Event, EventAdmin)
