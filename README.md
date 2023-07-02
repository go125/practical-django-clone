# practical-django-clone
- [実践Django Pythonによる本格Webアプリケーション開発](https://github.com/c-bata/practical-django)の練習

## 起動

```
docker compose up -d --build
```

## Pythonコンテナへの接続

```
docker compose exec python3 bash
```

### パッケージのインストール(初回起動時)

- 毎回「pip install -r requirements.txt」しなければならないのはあまりスマートではないため、今後の課題とする

```
cd src
pip install -r requirements.txt
```

### Djangoプロジェクトの作成(初回起動時)

```
django-admin startproject djangosnippets
cd djangosnippets
```

- DBと言語の設定を実施する
- 以下のコマンドで初期設定が完了したことを確認する
  - 「localhost:8081」からアクセス

```
python manage.py migrate
python manage.py runserver 0.0.0.0:8081
```

- ユーザ名：admin、メールアドレス：admin@example.com、パスワード：passwordの管理用ユーザーを作成
    - DBを残していれば、この作業は一度だけ行えばよい

```
python manage.py createsuperuser
```

### Djangoアプリケーションの作成

- settings.pyに"snippets.apps.SnippetsConfig"を忘れずに追加する

```
python manage.py startapp snippets
```

### ルーティングの実施

- コンテンツを仮置きして、ルーティングを先に行うのが定石である

### Modelの作成

- DBへの反映(migrate)を忘れずに実施する

### テンプレートの設置

- "snippets/static/snippets/css/style.css"を作成する
- base.htmlを作成する
  - base.htmlの作成場所に注意する

### ユーザー認証の作成

```
python manage.py startapp accounts
```

## pgAdminの設定

- 「localhost:8080」からアクセス
    - メールアドレス：example@example.com、パスワード：password
- ホスト名が「service_postgres」であることに注意すると接続できる
