# -*- coding: utf-8 -*-

from trello import TrelloClient
import pprint
from datetime import datetime,timezone,timedelta,date
import requests
import json
import unicodedata
import calendar
import csv
from common import is_japanese,init_py_trello,init_myboard

if __name__ == '__main__':
	# 日付の取得
	day_name_dict = {0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
	day_number_dict = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
	day_name_list = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	weekday = date.today().weekday()
	weekday_name = calendar.day_name[weekday]

	# py-trello client init
	# 設定ファイルから呼び出し
	client = init_py_trello()

	# board読み込み
	board = client.get_board(init_myboard())

	# メンバー一覧
	members = board.all_members()
	# リスト一覧
	lists = board.open_lists()
	# 書き込みファイルを選択
	f = open('output.csv', 'a')
	writer = csv.writer(f, lineterminator='\n')
	# 完了リストの情報を呼び出し、最後にリスト毎削除する。
	print("===================================================")
	for l in lists:
		
		JUDGE = is_japanese(l.name)
		if JUDGE:
			continue
		print("list name: {}".format(l.name))
		print("===================================================")
		target_list = board.get_list(l.id)
		cards = target_list.list_cards()
		for c in cards:
			csvlist = []
			csvlist.append(l.name)
			csvlist.append(c.name)
			csvlist.append(c.description)
			tmp = ""
			for la in c.labels:
				print(la)
				tmp = tmp + "[" + str(la) + "]"
			csvlist.append(tmp)
			
			tmp = ""
			for m in c.member_id:
				tmp = tmp + "[" + client.get_member(m).full_name + "]"
			csvlist.append(tmp)
			writer.writerow(csvlist)
		l.close()
	f.close()
	# listを初期化
	for day in day_name_list:
		diff_day = day_number_dict[day] - weekday
		the_day = date.today() + timedelta(days=diff_day)
		board.add_list(day + ":" + datetime.strftime(the_day, '%Y-%m-%d'),pos='bottom')
	stay_l = board.get_list('5bbed78897b2635c868cecb6')
	stay_l.move('bottom')
