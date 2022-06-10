import gpytorch
import torch


def predict(x_new, likelihood, model):
    # 推論モードに設定
    likelihood.eval()
    model.eval()

    with torch.no_grad(), gpytorch.settings.fast_pred_var():
        # 予測分布の出力
        prediction = likelihood(model(x_new))
        # 信用区間の出力
        lower, upper = prediction.confidence_region()
            
    return {"prediction": prediction, "lower": lower, "upper": upper}
