#!/usr/bin/env python3
import praw
import sys


USERNAME = "user"
PASSWORD = "pass"
USER_AGENT = "@noreply reddit bot, contact FOO for info"
AUTOREPLY_MSG = """\
This is an automated reply.

No one checks the inbox for this reddit account. Please contact me at /u/foo"""


def main():
    r = praw.Reddit(user_agent=USER_AGENT)
    r.login(USERNAME, PASSWORD)

    for msg in r.get_unread(unset_has_mail=True,
                            update_user=True):
        if isinstance(msg, praw.objects.Message):
            msg.reply(AUTOREPLY_MSG)
            msg.mark_as_read()
            print(msg, file=sys.stderr)


if __name__ == '__main__':
    main()