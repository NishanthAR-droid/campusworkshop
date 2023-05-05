"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaad3ak728r886a0stg-a.oregon-postgres.render.com",
        database="todo_l8fk",
        user="todo_l8fk_user",
        password="Px4LFtcEKGiAA8TgUyh7WAXymTZRS7vs")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
