"""
The flask application package.
"""
import os
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'Booklog.db')
)

# アプリケーションコンテキストが終了したときに
# 毎回DBを切断する
from .db import close_db
app.teardown_appcontext(close_db)

# インデックスページの読み込み
import Booklog.views

# ログイン機能の追加
import Booklog.auth
app.register_blueprint(auth.bp)

# 書籍管理機能の追加
import Booklog.book
app.register_blueprint(book.bp)