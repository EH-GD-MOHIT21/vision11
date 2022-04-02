from django.db import models
from usermanagerAPP.models import User1

# Create your models here.

class Chat(models.Model):
    user=models.ForeignKey(User1,on_delete=models.CASCADE)
    group=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField(null=True)

    def __str__(self):
        return(self.message)