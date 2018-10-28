import sys
from common import is_japanese,init_py_trello,init_myboard
from datetime import datetime,timezone,timedelta,date
import calendar

if __name__ == '__main__':
	
	args = sys.argv
	board_name = args[1]
	# 日付の取得
	day_name_dict = {0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
	day_number_dict = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
	day_name_list = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	weekday = date.today().weekday()
	weekday_name = calendar.day_name[weekday]

	client = init_py_trello()
	created_board = client.add_board(board_name, permission_level='private')
	open_lists = created_board.open_lists()
	for ol in open_lists:
		ol.close()
	shortcut = created_board.add_list('ショートカット',pos='bottom')
	worry = created_board.add_list('気になること',pos='bottom')
	todo = created_board.add_list('Todoリスト',pos='bottom')
	today = created_board.add_list('今日中',pos='bottom')
	doing = created_board.add_list('作業リスト',pos='bottom')
	for day in day_name_list:
		diff_day = day_number_dict[day] - weekday
		the_day = date.today() + timedelta(days=diff_day)
		created_board.add_list(day + ":" + datetime.strftime(the_day, '%Y-%m-%d'),pos='bottom')
	created_board.add_list('中断',pos='bottom')
	# shortcut.
	sys.exit(0)
