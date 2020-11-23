# import requests
# import mysql.connector
# from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, redirect, request, render_template, session

# with open("file.txt", "r") as f:
#     secret = f.read()

# mydb_conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password=secret,
#     database=""
# )
# finance_db = mydb_conn.cursor()