# DjangoによるWebアプリケーション制作

## 要件
スレッド作成
ユーザ登録

## Model
- User
  - name(char)
  - pass(char)
  - is_super(bool)

- Thread
  - name

- Post
  - message(text)
  - updated_at(date)

## 手順メモ
- `django-admin startproject "project_name"`
  - "project_name"ディレクトリにsettingやurlなどが追加される
- `cd "project_name"`
- `python manage.py migrate`: データベース作成
- `python manage.py runserver`: サーバー起動
- `python manage.py "app_name"`: アプリケーション追加
  - "app_name"ディレクトリにModelやViewが追加される
- modelにモデルを追加→settingにアプリを追加→viewにモデルの操作や表示を記述(htmlなども)→urlsでurlとviewを紐付け
- modelを作ってアプリを追加したら`python manage.py makemigrations`でモデルを作成→`python manage.py migrate`でデータベースへ
