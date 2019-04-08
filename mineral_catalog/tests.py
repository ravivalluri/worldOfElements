from django.core.paginator import Paginator
from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from mineral_detail.models import Mineral


class MineralIndexViewTests(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_letter_search(self):
        searched_letter = 'b'
        filtered_minerals = Mineral.objects.filter(name__startswith=searched_letter)

        resp = self.client.get(reverse('index'), {'letter': searched_letter})

        self.assertEqual(list(resp.context['minerals']), list(filtered_minerals))
        self.assertEqual(resp.context['searched_letter'], searched_letter)

    def test_group_search(self):
        searched_group = 'Borates'
        filtered_minerals = Mineral.objects.filter(group__name=searched_group)

        resp = self.client.get(reverse('index'), {'group': searched_group})

        self.assertEqual(list(resp.context['minerals']), list(filtered_minerals))
        self.assertEqual(resp.context['searched_group'], searched_group)

    def test_category_search(self):
        searched_category = 'Arsenic'
        filtered_minerals = Mineral.objects.filter(categories__name=searched_category)

        resp = self.client.get(reverse('index'), {'cat': searched_category})

        self.assertEqual(list(resp.context['minerals']), list(filtered_minerals))
        self.assertEqual(resp.context['searched_category'], searched_category)

    def test_search_box_search(self):
        """Tests that the 'fulltext query' is searching all the correct fields. This has been hardcoded."""

        search_box_query = 'ite'
        page = 1

        filtered_minerals = Mineral.objects.filter(
            Q(group__name__icontains=search_box_query) |
            Q(categories__name__icontains=search_box_query) |
            Q(name__icontains=search_box_query) |
            Q(image_filename__icontains=search_box_query) |
            Q(image_caption__icontains=search_box_query) |
            Q(formula__icontains=search_box_query) |
            Q(strunz__icontains=search_box_query) |
            Q(crystal_system__icontains=search_box_query) |
            Q(unit_cell__icontains=search_box_query) |
            Q(color__icontains=search_box_query) |
            Q(crystal_symmetry__icontains=search_box_query) |
            Q(cleavage__icontains=search_box_query) |
            Q(mohs_scale__icontains=search_box_query) |
            Q(luster__icontains=search_box_query) |
            Q(streak__icontains=search_box_query) |
            Q(diaphaneity__icontains=search_box_query) |
            Q(optical_prop__icontains=search_box_query) |
            Q(refractive_index__icontains=search_box_query) |
            Q(crystal_habit__icontains=search_box_query) |
            Q(specific_gravity__icontains=search_box_query)
        ).distinct()

        resp = self.client.get(reverse('index'), {'search-box': search_box_query})

        paginator = Paginator(filtered_minerals, 101)
        filtered_minerals = paginator.get_page(page)

        self.assertEqual(list(resp.context['minerals'].object_list), list(filtered_minerals.object_list))
        self.assertEqual(resp.context['search_term'], search_box_query)
