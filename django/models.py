from djanog.db import model
class Person(models.Model):
	name = models.BooleanField(default='ss')
	updated_on = DateTimeField(auto_now=True)
