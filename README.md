# API仕様
- 機能：顧客情報の取得
- パス：Users/:userId
- メソッド：GET

# 使用方法

```bash
$ python -m venv venv_py39
$ pip install -r requirements.txt
$ python ./import.py
$ python ./api.py
$ curl -i http://0.0.0.0:3000/users/Us0ymuik | jq -R 'fromjson?'
```


## Example
```bash
$ curl -i http://0.0.0.0:3000/users/Us0ymuik | jq  -R 'fromjson?'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0     100   156  100   156    0     0  15277      0 --:--:-- --:--:-- --:--:-- 78000
{
  "data": {
    "userCompany": "密林コンプライアンス印刷",
    "userDiscountRate": 46,
    "userId": "Us0ymuik"
  },
  "result": true

```

# 参考文献

https://qiita.com/Morinikiz/items/c2af4ffa180856d1bf30
