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


def message_template(date, title):
    """Template of the message we are willing to send"""
    message = email.message.EmailMessage()
    weekday = dow(date)
    message["Subject"] = f'Meeting reminder: "{title}"'
    message.set_content(
        f"""
Hi all!

This is a quick mail to remind you all that we have meeting about:
"{title}"
the {weekday} {date}.

See you there.
"""
    )
    return message


def send_message(message, emails):
    """ Send the message to the selected email
    """
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login("kballadares996@gmail.com", "ufxouekcqbavlutz")
    print("Login Success!")
    for email in emails.split(","):
        del message["To"]
        message["To"] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    """ Run The program and all the functions
    """
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split("|")
        #user, password = sys.argv[2].split("|")
        #print(user)
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email due to: {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
