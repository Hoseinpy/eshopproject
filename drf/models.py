from django.db import models
from account.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500, blank=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todos'


class Currency(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    changes = models.IntegerField()

    def __str__(self):
        return self.name