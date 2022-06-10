import torch


# 真の関数
def _true_func(x):
    return torch.exp(x) * torch.sin(2*torch.pi * x)


def noised_true_func(x, noise_scale=0.1):
    return _true_func(x) + noise_scale*torch.randn(len(x))
