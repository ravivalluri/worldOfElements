import random

from django.test import TestCase
from django.urls import reverse

from .models import Mineral, Group, Category


class MineralModelTests(TestCase):

    def setUp(self):
        self.new_group = Group.objects.create(name='test_group')
        self.new_group.save()

        self.new_category = Category.objects.create(name='test_category')
        self.new_category.save()

        self.new_mineral = Mineral.objects.create(
            name='Test',
            group=self.new_group,
        )
        self.new_mineral.save()
        self.new_mineral.categories.add(self.new_category.pk)

    def test_group_name(self):
        name = "test_group"

        group = Group.objects.get(name=name)
        self.assertEqual(str(group), name)
        self.assertEqual(group.name, name)

    def test_category_name(self):
        name = "test_category"

        category = Category.objects.get(name=name)
        self.assertEqual(str(category), name)
        self.assertEqual(category.name, name)

    def test_mineral_name(self):
        name = "Test"

        mineral = Mineral.objects.get(name=name)
        self.assertEqual(str(mineral), name)
        self.assertEqual(mineral.name, name)

    def test_mineral_url(self):
        static_url = 'images/minerals/Test.jpg'

        self.assertEqual(self.new_mineral.static_url, static_url)

    def test_mineral_first_name(self):
        self.assertEqual(self.new_mineral.first_name(), "Test")


class MineralDetailViewTests(TestCase):
    def setUp(self):
        self.new_group = Group.objects.create(name='test_group')
        self.new_group.save()

        self.new_category = Category.objects.create(name='test_category')
        self.new_category.save()

        self.new_mineral_1 = Mineral.objects.create(
            name='Test1',
            group=self.new_group,
        )
        self.new_mineral_1.save()
        self.new_mineral_1.categories.add(self.new_category.pk)

        self.new_mineral_2 = Mineral.objects.create(
            name='Test2',
            group=self.new_group,
        )
        self.new_mineral_2.save()
        self.new_mineral_2.categories.add(self.new_category.pk)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/detail/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_random_mineral(self):
        rand_num = random.randint(1, 2)

        resp = self.client.get(reverse('mineral_detail',
                                       kwargs={'mineral_id': rand_num}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('mineral_detail',
                                       kwargs={'mineral_id': 2}))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'detail.html')

    def test_404(self):
        resp = self.client.get(reverse('mineral_detail',
                                       kwargs={'mineral_id': 1000}))
        self.assertEqual(resp.status_code, 404)
