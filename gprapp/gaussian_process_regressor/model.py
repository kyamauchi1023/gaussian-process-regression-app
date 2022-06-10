import gpytorch


# ガウス過程回帰モデルの実装
class ExactGPModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood, kernel):
        super(ExactGPModel, self).__init__(train_x, train_y, likelihood)
        # 平均関数
        self.mean_module = gpytorch.means.ConstantMean()
        # カーネル関数
        if kernel == 'RBFKernel':
            self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())
        elif kernel == 'CosineKernel':
            self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.CosineKernel())
        elif kernel == 'LinearKernel':
            self.covar_module = gpytorch.kernels.LinearKernel()
        elif kernel == '2d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=2)
        elif kernel == '3d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=3)
        elif kernel == '4d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=4)
        elif kernel == '5d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=5)
        elif kernel == '6d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=6)
        elif kernel == '7d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=7)
        elif kernel == '8d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=8)
        elif kernel == '9d-PolynomialKernel':
            self.covar_module = gpytorch.kernels.PolynomialKernel(power=9)
    
    # ガウス過程の生成過程
    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)
