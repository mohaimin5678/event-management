from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=250)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name='events'
    )

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    total_events = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name