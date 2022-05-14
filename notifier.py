import time 

from plyer import notification #for getting notification on your PC

minute = 60

# Real:
no_study_sessions = 0
study_session_length = 25 # mins
break_length = 5 # mins
total_hours = 0

# for test:
# study_session_length = 25
# break_length = 15


app_icon_path = "bell.ico"

on_break = False
while(True):
	on_break = not on_break

	if on_break:
		print("Study")

		time.sleep(3)
		no_study_sessions += 1

		msg = "Session {s_sessions} starts. Total hours : {t_h}\n".format(s_sessions = no_study_sessions, t_h = total_hours)
		notification.notify(title = "Study time!", message = msg, app_icon = app_icon_path, timeout = 1)

	else:
		print("Break")
		time.sleep(3)
		total_hours += study_session_length / minute

		msg = "Session {s_sessions} ends. Total hours : {t_h}\n".format(s_sessions = no_study_sessions, t_h = total_hours)
		notification.notify(title = "Break time!", message = msg, app_icon = app_icon_path, timeout = 1)		