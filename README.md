# ガウス過程回帰を試してみよう！

ガウス過程回帰を簡単に体験できるWebアプリです.

WebフレームワークにはDjangoを, ガウス過程回帰の実装にはGPyTorchを使っています.

## Set Up
```shell
$ pip install -r requirements
$ python manage.py runserver
```
サーバーが立ったら[http://127.0.0.1:8000/gprapp/](http://127.0.0.1:8000/gprapp/)にアクセスしてください.

## 使い方

### 1. カーネル関数の種類を選択
まず, ガウス過程回帰に用いるカーネル関数を選択してください. 選択できるカーネル関数は以下のいずれかです.
- RBFKernel
- CosineKernel
- LinearKernel
- nd-PolynomialKernel(n = 2, ..., 9)

これらの関数の詳細は[GPyTorchの公式ドキュメント](https://docs.gpytorch.ai/en/v1.5.1/kernels.html)を参照してください.

### 2. ノイズのスケール${\delta}$を選択
元の信号は元の信号は以下の式に従って生成されています.
$$ f(t) = e^{t} sin({2\pi t}) + {\delta\varepsilon} $$
ここで, ${\varepsilon}$は標準正規分布からサンプリングされたノイズで, ${\delta}$倍されて真の関数に加算されています.
${\delta}$を調整することでノイズの影響の大きさを調整することができます.  この信号に対してガウス過程回帰を実行します.

### 3. train dataの数(1〜500の整数)を入力
train dataの数を1〜500の整数から選択してください.  train dataの数多くするほど信用区間が小さくなることを確認できると思います.

### 4. シード値(自然数)を入力
これを入力することでシード値を固定することができます.
