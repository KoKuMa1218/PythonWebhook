from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # รับข้อมูล JSON จาก Line Messaging API
    # ประมวลผลข้อมูลที่คุณได้รับที่นี่
    # ตัวอย่างการส่งคำตอบกลับ
    response = {
        "replyToken": data['events'][0]['replyToken'],
        "messages": [
            {
                "type": "text",
                "text": "สวัสดีจาก Webhook ของคุณ"
            }
        ]
    }
    # ส่งคำตอบกลับไปยัง Line Messaging API
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
