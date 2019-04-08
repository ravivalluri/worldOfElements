from django import forms

from .models import Mineral

class MineralForm(forms.ModelForm):
    class Meta:
        model = Mineral
        fields = ['strunz', 'crystal_system', 'cleavage', 'mohs_scale',
                  'unit_cell', 'color', 'crystal_symmetry',
                  'luster', 'streak', 'diaphaneity', 'optical_prop',
                  'refractive_index', 'crystal_habit',
                  'specific_gravity']
        labels = {
            'strunz': 'Strunz Classification',
            'mohs_scale': 'Mohs Scale Hardness'
        }