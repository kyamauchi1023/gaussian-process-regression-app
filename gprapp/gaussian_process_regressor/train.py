import gpytorch
import torch

from .model import ExactGPModel


def train(train_x, train_y, kernel='RBF'):
    # 尤度にガウス分布を設定
    likelihood = gpytorch.likelihoods.GaussianLikelihood()
    # モデルのインスタンス化
    model = ExactGPModel(train_x, train_y, likelihood, kernel)

    # ハイパーパラメータ学習モードに設定
    model.train()
    likelihood.train()

    # optimizerにAdamを設定
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1) 

    # 周辺対数尤度の計算
    mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)

    training_iter = 150
    loss_list = []
    for i in range(training_iter):
        # 勾配を0に初期化
        optimizer.zero_grad()
        # モデルからの出力
        output = model(train_x)
        # 損失関数の計算
        loss = -mll(output, train_y)
        # 勾配計算
        loss.backward()
        # パラメータ更新
        optimizer.step()
        loss_list.append(loss.detach().numpy())

    return {"likelihood": likelihood, "model": model}
