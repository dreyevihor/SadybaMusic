from django.db import models

# Create your models here.

class Schema_hall(models.Model):
	name = models.CharField(max_length = 100)


class Rows(models.Model):
	hall = models.ForeignKey(Schema_hall, related_name = 'rows' ,on_delete = models.CASCADE, null = False)
	number = models.IntegerField()
	place_from = models.IntegerField()
	place_to = models.IntegerField()
	class Meta():
		unique_together = ('hall', 'number')
