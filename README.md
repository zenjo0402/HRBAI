# HRBAI

Google Colab 等から HRBAI バックエンドへ安全にメッセージを送信するための Python パッケージです。

## インストール方法

Google Colab などの Python 環境で以下を実行してインストールします。


!pip install --force-reinstall --no-cache-dir git+[https://github.com/zenjo0402/HRBAI.git](https://github.com/zenjo0402/HRBAI.git)

## 基本的な使い方
hrbai をインポートし、割り当てられた API キー（hrb-xxxx）と質問文を指定して send() 関数を呼び出します。

# SEND{}
import hrbai

hrbai.send("APIキー", "送信するメッセージ")


# HRBClient{}

GAS（Google Apps Script）と通信し、新しい API キーを自動発行・取得するためのクライアントクラスです。
