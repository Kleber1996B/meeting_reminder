#!/bin/bash

meeting_info=$(zenity --forms \
	--title 'Meeting' --text 'Reminder information' \
	--add-calendar 'Date' --add-entry 'Title' \
	--add-entry 'Emails' \
	2>/dev/null)

