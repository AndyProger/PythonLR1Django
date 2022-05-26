from django.db import models


class Links(models.Model):
    linkURL = models.CharField('Link', max_length=300)
    counter = models.IntegerField('Counter')

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
