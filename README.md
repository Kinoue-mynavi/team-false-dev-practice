## Team False Git/Github運用手順

### 導入

#### 1.リポジトリのクローン

#### 2. 作業したいディレクトリに移動する

- 井上の場合

```shell
cd ~/projects/mujiqlo
```

#### 3. リポジトリをクローンする

```shell
git clone https://github.com/Kinoue-mynavi/team-false-dev-practice.git
```

#### 4. クローンされたディレクトリに移動する

```shell
cd team-false-dev-practice
```

下記の「作業開始時」の手順に従って、作業を開始する。

### 作業開始時

- developを最新の状態にする

```shell
git pull origin develop
```

- 作業ブランチを作成する

```shell
git checkout -b 【your-branch-name】
```

### 作業終了時

#### ステージング + コミットする

```shell
git add .

git commit -m "【commit messages】"
```

#### リモートリポジトリ（Github）にプッシュする

```shell
git push origin 【your-branch-name】
```

#### Githubにアクセスし、Pull Requestを作成する

https://github.com/Kinoue-mynavi/team-false-dev-practice

を開き、

1. 画面上部に表示されるアラートからPull Requestを作成する
2. 概要欄に記載のチェックボックスの事項を確認する
3. 2の確認を終えたら「Create Pull Request」ボタン押下でPRを作成する。

### 自分のブランチがGithub上でMergeされたら

#### ローカルでdevelopブランチに移動

```shell
git checkout develop
```

#### 最新のdevelopをPULL

```shell
git pull origin develop
```

#### 再度、作業ブランチを作成して作業開始

```shell
git checkout -b 【新しい作業ブランチ名】
```

作業開始！

### コンフリクトを解消する

#### ローカルでdevelopブランチに移動

```shell
git checkout develop
```

#### 最新のdevelopをPULL

```shell
git pull origin develop
```

#### 最新のdevelopを自分の作業ブランチにマージする

```shell
git merge develop
```

#### 上記によって、コンフリクトが発生するので解消する

```
↓ developの変更（他の人の変更）
>>>>>> develop

<<<<<<

↓ head (自分の作業ブランチの変更)
>>>>>> head

<<<<<<
```

- 自分の変更が「正」の場合、`>>>>>> develop`部分を削除する
- 他の人の変更が「正」の場合、`>>>>>> head`部分を削除する
- 最後に、`<<<<`or`>>>>`等でコード検索して、検索結果が見つからなければOK
- コマンドラインにエディタが出現した場合、`Esc`を押下後、`:wq`を入力し保存して抜ける。

#### （コンフリクト解消後）ステージング + コミットする

```shell
git add .

git commit -m "resolve conflict"
```

#### 再度プッシュする

```shell
git push origin 【your-branch-name】
```

### 誤ってコミットしてしまったら、、、

- 直前のコミットをリセットする（Gitの履歴に残らない）

```shell
git reset --soft HEAD^
```

- ステージングを解除する

```shell
git restore --staged .
```

### 手元の差分を退避させたい場合、、、

- 現在の差分を退避

```shell
git stash -u
```

- 退避させた変更を表示

```shell
git stash list
```

- 退避させた変更を再度適応
    - git pull後などに行う。
    - ※過去に退避した結果があるかもしれないので、`stash@{0}`の番号に注意して適応する。（0とは限らない。）

```shell
git stash apply stash@{0}
```

## 2024 年新人研修向けムジクロチケット実行手順

### １.データベース作成

<VSCode のターミナルで実行>

```c
mysql -u root -p
```

password：mysql

```c
create database mujiqlo_ticket;
```

### 2.パッケージのインストール　※Flask 研修で実施済み

以下を**全文**コピーしてターミナルに貼り付け、実行。

```c
pip install click==8.0.4\
    Flask==1.1.2\
    Flask-Script==2.0.6\
    Flask-SQLAlchemy==2.5.1\
    greenlet==1.1.2\
    itsdangerous==2.0.1\
    Jinja2==3.0.3\
    MarkupSafe==2.1.1\
    PyMySQL==1.0.2\
    setuptools==54.2.0\
    SQLAlchemy==1.4.32\
    Werkzeug==2.0.3\
    cryptography==39.0.2
```

パッケージのインストール状況は以下のコマンドで確認

```c
pip list
```

### 3.テーブル作成

<VSCode のターミナルで実行>

・mujiqlo ディレクトリに移動して実行

```c
python manage.py init_db
```

### 4.ムジクロチケットの実行

<VSCode のターミナルで実行>

```c
python server.py
```

・chrome で http://127.0.0.1:5000/ にアクセスする
・'staff001','password'でログインする

---

<memo>
開発に使った環境
Python 3.9.4

Package Version

---

- click 8.0.4
- Flask 1.1.2
- Flask-SQLAlchemy 2.5.1
- greenlet 1.1.2
- itsdangerous 2.0.1
- Jinja2 3.0.3
- MarkupSafe 2.1.0
- pip 21.0.1
- PyMySQL 1.0.2
- setuptools 54.2.0
- SQLAlchemy 1.4.32
- Werkzeug 2.0.3
