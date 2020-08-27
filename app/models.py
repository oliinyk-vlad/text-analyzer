from django.db import models


class Text(models.Model):
    content = models.TextField(max_length=5000)

    def rarely(self):
        """ 3% >= count """
        return self.words.filter(count__lte=int(self.words.count() * 0.03))

    def medium(self):
        """ 3% < count < 5% """
        return self.words.filter(count__gt=int(self.words.count() * 0.03), count__lt=int(self.words.count() * 0.05))

    def often(self):
        """ 5% <= count """
        return self.words.filter(count__gte=int(self.words.count() * 0.05))


class Word(models.Model):
    text = models.ForeignKey(Text, related_name='words', on_delete=models.CASCADE)
    content = models.TextField()
    count = models.PositiveIntegerField()

    class Meta:
        ordering = ['-count']
