from django.db import models

class Mark(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=150)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
