from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage


app = Flask(__name__)

# กำหนดคีย์สำหรับ Line Messaging API
CHANNEL_SECRET = 'b49531f17c78c230bc5a82a1b264b22c'
CHANNEL_ACCESS_TOKEN = 'RnlMj2C+Gddj86Z7Z2oZiK/YiO+uvHLqQXqf6YEhLr5iCFWgeGsoCpTRIGUzk9+S7FYpizNtyUtpPprKUvqc25iqstZjhCqfkYVgpeuxAdCLO705lxQ5jMWyOVKIhqFyYbMViJ6XWruvkKh35RDKNgdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # รับข้อมูล Webhook จาก Line
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ตอบกลับข้อความ
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=event.message.text)
    )

if __name__ == "Webhook":
    app.run()
