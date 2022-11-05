#!/bin/bash

meeting_info=$(zenity --forms \
	--title 'Meeting' --text 'Reminder information' \
	--add-calendar 'Date' --add-entry 'Title' \
	--add-entry 'Emails' \
	--forms-date-format='%Y-%m-%d' \
	2>/dev/null)

ENTRY= zenity --forms --title="Login" \
	--text="Enter your password" \
	--add-entry="User" \
	--add-entry="Password" \

if [[ -n "$meeting_info" ]] ; then
	python3 send_reminders.py "$meeting_info" "$ENTRY"
fi
