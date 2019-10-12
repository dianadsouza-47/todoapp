from django.db import models


class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name

class Todo(models.Model):

    status_choice=(

        ('1','created'),
        ('2','in_progress'),
        ('3','done'),
      

    )
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=30)
    status=models.CharField(max_length=20,choices=status_choice)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# Create your models here.
