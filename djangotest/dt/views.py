from django.shortcuts import render
from django.core.paginator import Paginator

from dt.models import Record, RecordPage


def index(request):
    PER_PAGE = 48

    paginate = request.GET.get('paginate', None)
    page = int(request.GET.get('page', 1))

    count = Record.objects.filter(active=True).count()
    page_count = count // PER_PAGE + int(bool(count % PER_PAGE))

    if page < 1:
        page = 1
    if page > page_count:
        page = page_count

    if page == 1:
        prev_page = None
    else:
        prev_page = page - 1

    if page == page_count:
        next_page = None
    else:
        next_page = page + 1

    if paginate is None:
        records = Record.objects.filter(active=True).order_by('name')
        pages = Paginator(records, 48)
        records = pages.page(page).object_list
    else:
        records_pages = RecordPage.objects\
            .filter(page=page)\
            .select_related('record')\
            .order_by('record__name')
        records = [rp.record for rp in records_pages]

    return render(
        request,
        'records.html',
        dict(
            records=records,
            prev_page=prev_page,
            next_page=next_page))
