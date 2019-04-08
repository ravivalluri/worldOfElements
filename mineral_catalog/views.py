import random
import string

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from mineral_detail.models import Mineral, Group, Category


def index(request):
    """
    Index view is used for showing and filtering minerals. Search box takes precedence over letter filtering.
    """

    search_box_query = request.GET.get('search-box', None)
    group_search_query = request.GET.get('group', None)
    category_search_query = request.GET.get('cat', None)
    searched_letter = None

    if search_box_query:
        query = Q(group__name__icontains=search_box_query) | Q(categories__name__icontains=search_box_query)
        for field in Mineral._meta.get_fields():
            if field.name not in ['id', 'group', 'categories']:
                query |= Q(**{field.name + '__icontains': search_box_query})
    elif group_search_query:
        query = Q(group__name=group_search_query)
    elif category_search_query:
        query = Q(categories__name=category_search_query)
    else:
        searched_letter = request.GET.get('letter', 'a')
        query = Q(name__istartswith=searched_letter)

    filtered_minerals = Mineral.objects.filter(query).distinct()

    all_mineral_ids = Mineral.objects.all().values('id')
    rand_num = random.randint(1, all_mineral_ids.count())

    paginator = Paginator(filtered_minerals, 101)
    page = request.GET.get('page')
    minerals = paginator.get_page(page)

    groups = Group.objects.values('name').order_by('name')
    categories = Category.objects.values('name').order_by('name')

    context = {
        'minerals': minerals,
        'rand_mineral': rand_num,
        'letters': string.ascii_lowercase,
        'searched_letter': searched_letter,
        'searched_category': category_search_query,
        'searched_group': group_search_query,
        'search_term': search_box_query,
        'mineral_groups': groups,
        'mineral_categories': categories,
    }

    return render(request, 'index.html', context)
