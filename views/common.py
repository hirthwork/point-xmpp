# -*- coding: utf-8 -*-
"""
Common commands (uncategorized).
"""
import settings
import os.path
from contextlib import closing
from point.util.env import env

DEF_HELP = 'Help is temporarily available here: http://%s/help/commands.' % settings.domain

def show_help():
    if env.user and env.user.id:
        _lang = env.user.get_profile('lang')
    else:
        _lang = settings.lang

    help_file = os.path.join(settings.i18n_dir, 'help-%s.txt' % _lang)
    help_msg = ""
    if not os.path.exists(help_file):
        return DEF_HELP
    try:
        with closing(open(help_file)) as f:
            help_msg = f.read()
            return help_msg
    except Exception:
        return DEF_HELP

def ping():
    return {'body': 'Pong.', '_presence': True}

