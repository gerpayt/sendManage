# coding: utf-8
import os

DEBUG = False

PASSWORD = ""

DBFILE = os.path.join(os.path.dirname(__file__), "database.db")

NOTICE_PERIOD = 90
NOTICE_MAIL = "gerpayt@qq.com"
NOTICE_NAME = u"某人"

SMTP_SERVER = "smtp.exmail.qq.com"
SMTP_PORT = 25
SMTP_USE_TLS = False
SMTP_USE_SSL = False
SMTP_USER = "xxx"
SMTP_USERNAME = u"文章到期提醒系统"
SMTP_PASSWORD = "xxx"
