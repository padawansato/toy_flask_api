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

# API の目的
- *プラットフォームの独立* API の内部実装に関係なく、すべてのクライアントが API を呼び出すことができる必要がある。そのためには、標準プロトコルを使用し、クライアントと Webサービス が交換するデータの形式に同意できるメカニズムを備えている必要がある。


# 用語
## REST とはなにか
2000 年に、ロイ・フィールディングが、Web サービスを設計するためのアーキテクチャアプローチとして Representational State Transfer (REST) を提唱した。

必ずしも アプリケーションプロトコルとして HTTP をサポートしなければならないわけではないが、一般的には HTTP が用いられる。

## RESTful API の主な設計原則

- REST API は "リソース" を中心に設計する。リソースとは、クライアントがアクセスできるあらゆる種類のオブジェクト、データ、またはサービスを指す。
- リソースにはそれを一意に識別できる"識別子"=URI がある。
- クライアントはリソースをなんらかの表現方法に変換してサービスと対話する。多くの Web API では交換形式として JSON を使用する。
- リソース操作に統一インターフェースを使用する。GET, POST, PUT, PATCH, DELETE が一般的。
- ステートレスな request モデルを使用する。HTTP リクエストは独立しており、任意の順序で発生する可能性がある。
	- リクエスト間の遷移状態の情報を保持することはできない。
	- 情報の格納場所はリソース自体のみであり、それぞれのリクエストはアトミックな操作である必要がある。
	- これにより、スケーラブルな Web サービスが実現される。クライアントと特定のサーバー間のアフィニティ(親和, 同期)を保持する必要がないため。どのサーバーも、任意のクライアントから要求を処理できる。

## エンドポイントとは
エンドポイントとは API にアクセスするための URI のこと。

## エントリーポイントとは
エンドポイントと似ているが、プログラムが絵トリーする場所という意味。
API の場合、URI が参照されるとき、プログラムが開始するため、URI がエントリーポイントである。

*エンドポイントとエントリーポイントの違いは、アクセスする視点の違い*


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

- リソース URI は動詞 (リソースに対する操作) ではなく、名詞 (リソース) に基づくようにします。

# 参考文献
- https://docs.microsoft.com/ja-jp/azure/architecture/best-practices/api-design
- https://qiita.com/Morinikiz/items/c2af4ffa180856d1bf30
- https://qiita.com/NagaokaKenichi/items/6298eb8960570c7ad2e9
