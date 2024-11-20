from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination(request, data, num=10):
    paginator = Paginator(data, num)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 2 #if index <= 2 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return items, page_range
