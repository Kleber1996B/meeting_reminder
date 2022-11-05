#!/usr/bin/env python3

""" To send reminders to user emails, from data inputed by the user
"""

import datetime
import email
import smtplib
import sys


def usage():
    """Print usage message in case of need"""
    print("send_reminders: Send meeting reminders\n")
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|Emails' ")
    return 1


def dow(date):
    """create datetime.datetim.strptime object from a str provided by the user"""
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def send_message(message, emails):
    smtp = smtp.SMTP("localhost")
    message["From"] = "noreply@example.com"
    for email in emails.split(","):
        del message["To"]
        message["To"] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split("|")
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
