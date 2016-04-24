from django.db import models


class Entry(models.Model):
    message = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return '<Entry> {author} @ {date}: "{short}..."'.format(
            author=self.author,
            date=self.date.strftime('%Y/%m/%d %H:%M'),
            short=self.message[:20],
        )
