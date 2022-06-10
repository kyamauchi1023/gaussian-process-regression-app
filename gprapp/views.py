import random

from django.views.generic import TemplateView
from django.shortcuts import render
import numpy as np
import torch

from .gaussian_process_regressor.graph import plot_graph
from .gaussian_process_regressor.predict import predict
from .gaussian_process_regressor.train import train
from .gaussian_process_regressor.true_func import noised_true_func
from . import forms


class Index(TemplateView):

    # テンプレートファイル連携
    template_name = "index.html"

    def __init__(self):
        self.context = {
            'kernel': 'RBFKernel',
            'noise_scale': 0.1,
            'train_x_size': 20,
            'seed': 42,
            'form': forms.ParamsForm(),
        }

    def get_context_data(self, **kwargs):
        return self.context

    # get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    #post処理
    def post(self, request, *args, **kwargs):

        form = forms.ParamsForm(self.request.POST)
        
        if form.is_valid():
            self.context['kernel'] = form.cleaned_data['kernel']
            self.context['noise_scale'] = float(form.cleaned_data['noise_scale'])
            self.context['train_x_size'] = int(form.cleaned_data['train_x_size'])
            self.context['seed'] = int(form.cleaned_data['seed'])
            self.context['form'] = form

        kernel = self.context['kernel']
        noise_scale = self.context['noise_scale']
        train_x_size = self.context['train_x_size']
        seed = self.context['seed']

        np.random.seed(seed)
        random.seed(seed)
        torch.manual_seed(seed)

        train_x = torch.linspace(-1, 1, train_x_size)
        train_y = noised_true_func(train_x, noise_scale)

        # 学習
        train_result = train(train_x, train_y, kernel)

        # 推論
        x = torch.linspace(-1, 1, 500)
        predict_result = predict(x, **train_result)

        # グラフを表示
        original_y = noised_true_func(x, noise_scale)
        chart = plot_graph(x, original_y, train_x, train_y, **predict_result)

        # 変数を渡す
        self.context['chart'] = chart

        return render(request, self.template_name, context=self.context)
