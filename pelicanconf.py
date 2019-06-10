#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huongnhd'
SITENAME = u'Huongnhd\'s journey '
SITESUBTITLE='Go Slow…To Go Fast!'
BANNERTITLE='Greatness Awaits'
SITEURL = ''
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

STATIC_PATHS = ['extra', 'images']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': SITEURL + 'favicon.ico'}
}

MENUITEMS = (
    ('Archives', '/archives'),
    ('Tags', '/tags'),
    ('Authors', '/authors'),
)

GITHUB_URL = 'https://github.com/huongnhdh/'

IMAGES_PATH = '{}/images/'.format(SITEURL)

# SERVER_PATH_SUFFIXES = ['.html', '/index.html', '/', '']
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}'

TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags'

TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}'

AUTHORS_SAVE_AS = 'authors/index.html'
AUTHORS_URL = 'authors'

AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL =  'author/{slug}'

CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories'

CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'

ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives'