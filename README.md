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

### 2. ノイズのスケール${\delta}$を入力
ノイズのスケールを0以上1以下の正数で入力してください.

観測データは以下の式に従って生成されています.
$$ f(t) = e^{t} sin({2\pi t}) + {\delta\varepsilon} $$
ここで, ${\varepsilon}$は標準正規分布からサンプリングされたノイズで, ${\delta}$倍されて真の関数に加算されています.
${\delta}$を調整することでノイズの影響の大きさを調整することができます.  このデータに対してガウス過程回帰を実行します.

### 3. 観測データ数を入力
観測データ数を1以上500以下の整数で入力してください.  観測データ数を多くするほど曖昧さが小さくなることを確認できると思います.

### 4. 実行ボタンを押す
「学習と推論を実行」というボタンを押してください.
