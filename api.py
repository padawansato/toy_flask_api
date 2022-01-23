from flask import Flask, jsonify, abort, make_response
import peewee

# db 接続
db = peewee.SqliteDatabase("data.db")

# ユーザーモデル定義
class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

# アプリケーション
api = Flask(__name__) 

# get
@api.route('/users/<string:userId>', methods=['GET'])
def get_user(userId):
    try:
        user = User.get(User.userId == userId)
    except DoesNotExist:
        abort(404)

    result = {
            "result": True,
            "data":{
                "userId": user.userId,
                "userCompany": user.userCompany,
                "userDiscountRate": user.userDiscountRate}}

    return make_response(jsonify(result))
#    return make_response(json.dumps(result, ensure_ascii=False))


# Error
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
