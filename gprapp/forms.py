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

    noise_scale = forms.fields.ChoiceField(
        initial = 0.1,
        label='ノイズのスケール',
        choices = (
            (0.0, 0.0),
            (0.1, 0.1),
            (0.2, 0.2),
            (0.3, 0.3),
            (0.4, 0.4),
            (0.5, 0.5),
        ),
        required=True,
        widget=forms.widgets.Select,
    )

    train_x_size = forms.IntegerField(
        initial = 20,
        label = 'train dataの数(1〜500の整数)',
        validators = [MinValueValidator(1), MaxValueValidator(500)],
        required = True,
    )

    seed = forms.IntegerField(
        initial = 42,
        label = 'シード値を指定',
        required = True,
    )
