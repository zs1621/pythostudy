# Create your views here.
from models import User, Person
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world.You're at the testdj1")

