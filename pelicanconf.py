#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huongnhd'
SITENAME = u'Huongnhd\'s journey '
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

LINKS = ()
# Social widget
SOCIAL = (
    ('github', 'https://github.com/huongnhdh'),
    #   ('linkedin', 'https://www.linkedin.com/in/huongnhd/'),
    #    ('email', 'mailto://huong.nhdh@gmail.com')
    )

DEFAULT_PAGINATION = 10
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
