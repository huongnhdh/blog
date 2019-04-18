#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huongnhd'
SITENAME = u'Huongnhd\'s journey '
SITESUBTITLE='Go Slow…To Go Fast!'
BANNERTITLE='Greatness Awaits'
SITEURL = 'http://local.blog:8080/'
PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
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
RELATIVE_URLS = False
THEME = "./notmyidea"
# custom for theme

# STATIC_PATHS = ['extra', 'images']

# EXTRA_PATH_METADATA = {
#     'extra/favicon.ico': {'path': SITEURL + 'favicon.ico'}
# }

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Tags', '/tags.html'),
    ('Authors', '/authors.html'),
)

GITHUB_URL = 'https://github.com/huongnhdh/'

IMAGES_PATH = '{}/images/'.format(SITEURL)