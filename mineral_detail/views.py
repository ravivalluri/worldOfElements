import random
import string

from django.shortcuts import render, get_object_or_404

from .forms import MineralForm
from .models import Mineral, Group, Category


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, pk=mineral_id)

    mineral_form = MineralForm(instance=mineral)

    all_mineral_count = Mineral.objects.all().values('id').count()
    rand_num = random.randint(1, all_mineral_count)

    groups = Group.objects.values('name').order_by('name')
    categories = Category.objects.values('name').order_by('name')

    context = {
        'mineral': mineral,
        'mineral_form': mineral_form,
        'rand_mineral': rand_num,
        'letters': string.ascii_lowercase,
        'mineral_groups': groups,
        'mineral_categories': categories,
    }

    return render(request, 'detail.html', context)
