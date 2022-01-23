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
| | | | 
| --- | --- | --- |
|userId|userCompany|userDiscountRate|
|Us0ymuik|密林コンプライアンス印刷|46|
|Us77qmr2|西日本密林エンターテイメント|49|
| ... | ... | ... |


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
# ベストプラクティス
## URIの基本的な設計
良いURIの設計で重要な原則は、
　*覚えやすく、どんな機能を持つURIなのかがひと目でわかる*
ということ。

## 一般的に良いとされるURIの重要な事項

1. 短くて入力しやすい
2. 人間が読んで理解できるURI
3. 大文字小文字が混在していないURI
4. サーバ側のアーキテクチャが反映されないURI
5. ルールが統一されたURI
6. バージョン番号が含まれたURI

# 参考文献
- https://docs.microsoft.com/ja-jp/azure/architecture/best-practices/api-design
- https://qiita.com/Morinikiz/items/c2af4ffa180856d1bf30
- https://qiita.com/NagaokaKenichi/items/6298eb8960570c7ad2e9
