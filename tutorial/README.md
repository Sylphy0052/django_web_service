# [参考](https://docs.djangoproject.com/en/2.1/): https://docs.djangoproject.com/en/2.1/

## Part1
- `python -m django --version` → `2.2.dev20181101005010`
- `django-admin startproject mysite`: プロジェクト作成
- `tree mysite`
```
mysite # rootディレクトリ
├── manage.py # Djangoのコマンドラインユーティリティ
└── mysite # プロジェクトのPythonパッケージ(mysite.urlsなどでimportする)
    ├── __init__.py # Pythonパッケージであることを伝える(編集しない)
    ├── settings.py # Djangoプロジェクトの設定
    ├── urls.py # DjangoプロジェクトのURL宣言
    └── wsgi.py # WSGI互換サーバのエントリーポイント

1 directory, 5 files
```
- `python manage.py runserver`: サーバ実行
```
Performing system checks…

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

November 01, 2018 - 21:26:15
Django version 2.2.dev20181101005010, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- `python manage.py startapp polls`: アプリ作成
- `tree polls`
```
polls
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
```
- `touch polls/urls.py`
- `polls/views.py`にrequestを受け取ってresponseを返す関数を書く
- `polls/urls.py`にviesの関数を使用することを書く
- `mysite/urls.py`にpathを書く
  - `include()`は他のURLconfsを参照できる．そのポイントまでにマッチしたURLを切り捨て，残った文字列をURLconfに送る

## Part2
- `python manage.py migrate`: データベースを作成/更新する．主に`mysite/settings.py`から読み込む
- `polls/models.py`にモデルを書く
  - `django.db.Models`をサブクラスにする
  - フィールドはデータタイプを指定する(IntやCharなど)
  - `ForeignKey`は1対多の関係
- `mysite/settings.py`のINSTALLED_APPを変更/追加
- `python manage.py makemigrations polls`でモデルを更新
  - 設定は`polls/migrations/0001_initial.py`などに書き込まれる
- `python manage.py migrate`でデータベースを更新
- 流れ:
  - Modelを書く
  - `python manage.py makemigrations`で変更のマイグレーションを作成
  - `python manage.py migrate`で変更をデータベースに適用する
- `python manage.py shell`で対話できる
- `python manage.py createsuperuser`で管理者を作成
- `http://127.0.0.1:8000/admin`で管理者画面へ
- `polls/admin.py`に管理者画面の設定をする

## Part3
- templates: `polls/templates/polls/~.html`
- viewを変更

## Part5
- Test
- `polls/tests.py`
- `python manage.py test polls`
