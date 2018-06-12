from django.contrib import admin


from Event.models import Event, Image_portfolio, Phones
#Register your models here.

class EventImagesInline(admin.StackedInline):
	model = Image_portfolio
	extra = 4


class PhoneInline(admin.StackedInline):
	model = Phones
	extra = 2

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	inlines = [EventImagesInline, PhoneInline]

admin.site.register(Event, EventAdmin)
