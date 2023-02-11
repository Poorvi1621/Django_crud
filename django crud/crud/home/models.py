from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=20)
    sal=models.IntegerField()
    address=models.TextField()
    def __str__(self) -> str:
        return self.name
