from django.contrib import admin


from Event.models import Event, Image_portfolio
#Register your models here.

class EventImagesInline(admin.StackedInline):
	model = Image_portfolio
	extra = 4

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	inlines = [EventImagesInline]

admin.site.register(Event, EventAdmin)
