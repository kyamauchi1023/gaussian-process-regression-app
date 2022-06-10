# ガウス過程回帰を試してみよう！

簡単にガウス過程回帰を体験できるWebアプリです.

## Set Up
```shell
$ pip install -r requirements
$ python manage.py runserver
```
サーバーが立ったら[http://127.0.0.1:8000/gprapp/](http://127.0.0.1:8000/gprapp/)にアクセスしてください.

## 使い方

### 1. カーネル関数の種類を選択
選択できるカーネル関数は, 
- RBFKernel
- CosineKernel
- LinearKernel
- nd-PolynomialKernel(n = 2, ..., 9)

詳しい中身は[GpyTorchの公式ドキュメント](https://docs.gpytorch.ai/en/v1.5.1/kernels.html)を参照してください.

### 2. ノイズのスケール${\delta}$を選択
元の信号は
$$ f(t) = e^{t} sin({2\pi t}) + {\delta\varepsilon,\ \ }{\ \ \varepsilon\ \ } 〜 {\ \ N(0, 1)}$$
となっています.
ただし, $N(0, 1)$は標準正規分布を表します.

${\delta}$を調整することでノイズの大きさを調整することができます.

### 3. train dataの数(1〜500の整数)を入力
train dataの数を1〜500の整数から選択してください.  train dataの数多くするほど信用区間が小さくなることを確認できると思います.

### 4. シード値(自然数)を入力
これを入力することでシード値を固定することができます.
