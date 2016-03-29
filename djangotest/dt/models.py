from django.db import models


class Record(models.Model):
    uts = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    name = models.CharField(max_length=256, db_index=True, unique=True)
    description = models.TextField(null=True)

    class Meta:
        index_together = (
            ('active', 'name', ), )


class RecordPage(models.Model):
    uts = models.DateTimeField(auto_now_add=True)

    record = models.OneToOneField(Record)
    page = models.PositiveIntegerField(db_index=True)

    class Meta:
        index_together = (
            ('record', 'page', ), )
        unique_together = (
            ('record', 'page', ), )
