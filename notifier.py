import time

from plyer import notification #for getting notification on your PC

minute = 60
hour = 60

no_study_sessions = 0
study_session_length = 25 * minute # seconds
break_length = 5 * minute # seconds
curr_mins = 0
total_hours = 0

app_icon_path = "bell.ico"

on_break = False
while(True):
	on_break = not on_break

	if on_break:
		no_study_sessions += 1

		msg = "Session {s_sessions} starts. Total : {t_h} hours and {t_m} minutes.\n".format(s_sessions = no_study_sessions, t_h = total_hours, t_m = curr_mins)
		notification.notify(title = "Study time!", message = msg, app_icon = app_icon_path, timeout = 1)

		time.sleep(study_session_length)

	else:
		curr_mins += study_session_length // minute
		total_hours += curr_mins // hour
		curr_mins -= total_hours * minute

		msg = "Session {s_sessions} ends. Total : {t_h} hours and {t_m} minutes.\n".format(s_sessions = no_study_sessions, t_h = total_hours, t_m = curr_mins)
		notification.notify(title = "Break time!", message = msg, app_icon = app_icon_path, timeout = 1)

		time.sleep(break_length)

	print(f"Study, hours: {total_hours}, mins: {curr_mins}")
