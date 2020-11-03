from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def post_order():
    name = request.form["name"]
    amount = request.form["amount"]
    address = request.form["address"]
    phone = request.form["phone"]

    doc = {
        'name': name,
        'amount': amount,
        'address': address,
        'phone': phone
    }
    db.myshop.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다 :>'})

@app.route('/order', methods=['GET'])
def show_order():
    goods = list(db.myshop.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'goods': goods})

if __name__ == '__main__':
    app.run()
