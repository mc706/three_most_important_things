from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Day(models.Model):
    account = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return self.account.username + str(self.date)

    def get_status(self):
        return sum([1 for task in self.task_set.all() if task.completed])

    class Meta:
        unique_together = ('account', 'date')
        verbose_name = 'day'
        verbose_name_plural = 'days'


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    day = models.ForeignKey(Day)
    priority = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('day', 'priority')
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
