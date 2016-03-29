from django.core.management.base import BaseCommand
from django.core.paginator import Paginator

from dt.models import Record, RecordPage


class Command(BaseCommand):
    help = 'Creates 10000 records'

    def handle(self, *args, **options):
        Record.objects.all().delete()

        records = []

        for i in range(10000):
            if i % 2 == 0:
                active = True
            else:
                active = False
            records.append(Record(active=active, name='record %d' % i,
                                  description='description %d' % i))
        Record.objects.bulk_create(records)

        RecordPage.objects.all().delete()

        records_pages = []

        records = Record.objects.filter(active=True).order_by('name')
        pages = Paginator(records, 48)

        for page in pages.page_range:
            for record in pages.page(page).object_list:
                records_pages.append(RecordPage(record=record, page=page))

        RecordPage.objects.bulk_create(records_pages)
