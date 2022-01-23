"""
データベースを作成、接続して、データを登録する。
SQL ではなく ORMマッパー Peewee を用いる。
"""

import peewee

# データベースを指定
db = peewee.SqliteDatabase("data.db")

# ユーザーモデルを定義


class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db


# ユーザーテーブル作成
User.create_table()

# データベースに登録
for line in open("seed_data/user.tsv", "r"):
    (userId, userCompany, userDiscountRate) = tuple(line[:-1].split("\t"))
    if userDiscountRate.isdigit():
        User.create(userId=userId,
                    userCompany=userCompany,
                    userDiscountRate=int(userDiscountRate))
