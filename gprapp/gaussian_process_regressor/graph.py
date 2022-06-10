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


# 元の信号のグラフをプロットするための関数
def _plot_original_graph(x, original_y):
	plt.scatter(x, original_y, s=10, label="original signal")


# 推論結果のグラフをプロットするための関数
def _plot_predicted_graph(x, train_x, train_y, prediction, lower, upper):
    plt.plot(train_x.numpy(), train_y.numpy(), 'k*', label='Observed Data', color='red')
    plt.plot(x.numpy(), prediction.mean.numpy(), 'b', label='Mean')
    plt.fill_between(x.numpy(), lower.numpy(), upper.numpy(), alpha=0.2, label='Confidence', color="green")


def plot_graph(x, original_y, train_x, train_y, prediction, lower, upper):
	plt.switch_backend("AGG")  # スクリプトを出力させない
	plt.figure(figsize=(10, 5))  # グラフサイズ
	_plot_original_graph(x, original_y)
	_plot_predicted_graph(x, train_x, train_y, prediction, lower, upper)
	plt.xticks(rotation=45)  # X軸値を45度傾けて表示
	plt.title("Gaussian Process Regression")  # グラフタイトル
	plt.xlabel("$t$")  # xラベル
	plt.ylabel("$f(t)$")  # yラベル
	plt.legend()
	plt.tight_layout()  # レイアウト
	graph = _output_graph()  # グラフプロット
	return graph
