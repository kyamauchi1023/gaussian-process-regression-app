import base64
from io import BytesIO

import matplotlib.pyplot as plt


# プロットしたグラフを画像データとして出力するための関数
def _output_graph():
	buffer = BytesIO()  # バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")  # png形式の画像データを取り扱う
	buffer.seek(0)  # ストリーム先頭のoffset byteに変更
	img = buffer.getvalue()  # バッファの全内容を含むbytes
	graph = base64.b64encode(img)  # 画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")  # デコードして文字列から画像に変換
	buffer.close()
	return graph


# 真の関数のグラフをプロットするための関数
def _plot_true_graph(x, true_y):
	plt.plot(x, true_y, label="true function", color="green")


# 推論結果のグラフをプロットするための関数
def _plot_predicted_graph(x, train_x, train_y, prediction, lower, upper):
    plt.scatter(train_x.numpy(), train_y.numpy(), s=30, label='Observed Data', color='red', marker="*")
    plt.plot(x.numpy(), prediction.mean.numpy(), 'b', label='Mean')
    plt.fill_between(x.numpy(), lower.numpy(), upper.numpy(), alpha=0.3, label='Confidence')


def plot_graph(x, true_y, train_x, train_y, prediction, lower, upper):
	plt.switch_backend("AGG")  # スクリプトを出力させない
	plt.figure(figsize=(10, 5))  # グラフサイズ
	_plot_true_graph(x, true_y)
	_plot_predicted_graph(x, train_x, train_y, prediction, lower, upper)
	plt.xlabel("$t$")  # xラベル
	plt.ylabel("$f(t)$")  # yラベル
	plt.legend()
	plt.tight_layout()  # レイアウト
	graph = _output_graph()  # グラフプロット
	return graph
