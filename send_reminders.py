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
