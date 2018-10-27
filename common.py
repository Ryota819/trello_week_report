# -*- coding: utf-8 -*-

import unicodedata
import configparser
from trello import TrelloClient

# 日本語含むか判定
def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False


# py-trello client init
# 設定ファイルから呼び出し
def init_py_trello():
	inifile = configparser.ConfigParser()
	inifile.read('./config.ini', 'UTF-8')
	my_api = inifile.get('py-trello','api')
	my_token = inifile.get('py-trello','token')
	client = TrelloClient(my_api, token=my_token)
	return client

def init_myboard():
	inifile = configparser.ConfigParser()
	inifile.read('./config.ini', 'UTF-8')
	my_board = inifile.get('py-trello','private')
	return my_board 

def init_mywork():
	inifile = configparser.ConfigParser()
	inifile.read('./config.ini', 'UTF-8')
	my_work = inifile.get('py-trello','work')
	return my_work
	