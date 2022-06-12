from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class ParamsForm(forms.Form):
    kernel = forms.fields.ChoiceField(
        initial = 'RBFKernel',
        label = 'カーネル関数の種類',
        choices = (
            ('RBFKernel', 'RBFKernel'),
            ('LinearKernel', 'LinearKernel'),
            ('CosineKernel', 'CosineKernel'),
            ('2d-PolynomialKernel', '2d-PolynomialKernel'),
            ('3d-PolynomialKernel', '3d-PolynomialKernel'),
            ('4d-PolynomialKernel', '4d-PolynomialKernel'),
            ('5d-PolynomialKernel', '5d-PolynomialKernel'),
            ('6d-PolynomialKernel', '6d-PolynomialKernel'),
            ('7d-PolynomialKernel', '7d-PolynomialKernel'),
            ('8d-PolynomialKernel', '8d-PolynomialKernel'),
            ('9d-PolynomialKernel', '9d-PolynomialKernel'),
        ),
        required=True,
        widget=forms.widgets.Select,
    )

    noise_scale = forms.FloatField(
        initial = 0.1,
        label = 'ノイズのスケール',
        validators = [MinValueValidator(0.0), MaxValueValidator(1.0)],
        required = True,
    )

    train_x_size = forms.IntegerField(
        initial = 10,
        label = '観測データ数',
        validators = [MinValueValidator(1), MaxValueValidator(500)],
        required = True,
    )
