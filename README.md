# HRBAI

Google Colab 等から HRBAI バックエンドへ安全にメッセージを送信するための Python パッケージです。

## インストール方法

Google Colab などの Python 環境で以下を実行してインストールします。

```python
!pip install --force-reinstall --no-cache-dir git+[https://github.com/zenjo0402/HRBAI.git](https://github.com/zenjo0402/HRBAI.git)
基本的な使い方
hrbai をインポートし、割り当てられた API キー（sk-hrbai-xxxx）と質問文を指定して send() 関数を呼び出します。

Python
import hrbai

# hrbai.send(APIキー, メッセージ)
hrbai.send("sk-hrbai-1234", "PYTHONってなに？")
関数の仕様
hrbai.send(api_key, message)
引数	型	説明	例
api_key	str	発行された個別の認証キー	"sk-hrbai-1234"
message	str	AIへ送信する質問やプロンプト	"PYTHONってなに？"
戻り値: なし (None)

出力: 送信成否のステータス（送信完了しました！ または エラーメッセージ）を標準出力します。
---
