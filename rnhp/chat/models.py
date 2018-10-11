from django.db import models


class Message(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.content


class MessageLike(models.Model):
    message = models.ForeignKey(
        Message,
        related_name='likes',
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Message like'
        verbose_name_plural = 'Message likes'
        unique_together = (('message', 'author'),)

    def __str__(self):
        return '{} +1'.format(self.author)
