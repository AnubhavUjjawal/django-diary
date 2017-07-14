from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GoogleUser(models.Model):
	google_id = models.CharField(max_length=300)
	nickname = models.CharField(max_length=10,unique=True)
	user = models.OneToOneField(User)

class Posts(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	post_title = models.CharField(max_length=50)
	post_body = models.TextField()

	@classmethod
	def create(cls, q):
		return cls(author=q['author'],post_title = q['post_title'],post_body= q['post_body'])

