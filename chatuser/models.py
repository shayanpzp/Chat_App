from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.Name}'



class Message(models.Model):
    user = models.ManyToManyField(User)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.Name}'