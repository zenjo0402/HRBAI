import requests

# 外部に見せない設定情報
_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeWapCRQAEOmJc5JjS3El660Tv4svqGnLy7lMT1SaF6hkq2eg/formResponse"
_ENTRY_KEY = "entry.1776600738"
_ENTRY_MSG = "entry.1669298738"

def send(api_key: str, message: str) -> None:
    """HRBAIへメッセージを送信する関数"""
    payload = {_ENTRY_KEY: api_key, _ENTRY_MSG: message}

    try:
        res = requests.post(_FORM_URL, data=payload)
        if res.status_code == 200:
            print("送信完了しました！")
        else:
            print(f"送信失敗 (Status: {res.status_code})")
    except Exception as e:
        print("エラーが発生しました:", e)
