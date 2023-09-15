from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

app = Flask(__name__)

# กำหนดคีย์สำหรับ Line Messaging API
CHANNEL_SECRET = 'YOUR_CHANNEL_SECRET'
CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN'

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

if __name__ == "__main__":
    app.run()
