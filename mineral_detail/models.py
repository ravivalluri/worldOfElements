from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Mineral(models.Model):
    name = models.CharField(max_length=500)
    image_filename = models.CharField(max_length=500)
    image_caption = models.CharField(max_length=500)
    formula = models.CharField(max_length=500, blank=True)
    strunz = models.CharField(max_length=500, blank=True)
    crystal_system = models.CharField(max_length=500)
    unit_cell = models.CharField(max_length=500, blank=True)
    color = models.CharField(max_length=500, blank=True)
    crystal_symmetry = models.CharField(max_length=500, blank=True)
    cleavage = models.CharField(max_length=500, blank=True)
    mohs_scale = models.CharField(max_length=500, blank=True)
    luster = models.CharField(max_length=500, blank=True)
    streak = models.CharField(max_length=500, blank=True)
    diaphaneity = models.CharField(max_length=500, blank=True)
    optical_prop = models.CharField(max_length=500, blank=True)
    refractive_index = models.CharField(max_length=500, blank=True)
    crystal_habit = models.CharField(max_length=500, blank=True)
    specific_gravity = models.CharField(max_length=500, blank=True)
    categories = models.ManyToManyField(Category)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def first_name(self):
        return self.name.split(", ")[0]

    @property
    def static_url(self):
        return 'images/minerals/' + self.name.title() + '.jpg'

    def category_names(self):
        return ', '.join([a.name for a in self.categories.all()])

    def __str__(self):
        return self.name
