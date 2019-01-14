from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.ticket.title + '-' + str(self.id)