#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Noelle'
SITENAME = 'She Builds With Code'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Custom paths and URLS for posts, pages & images
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_PATHS = ['pages', 'static-pages']
STATIC_PATHS = ['images', 'static-pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

# Summary limits for articles and pages
SUMMARY_MAX_LENGTH = 30

# Deactivating Cache for development
LOAD_CONTENT_CACHE = False

# Menu options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Other custom settings

# Switch what is commented out when testing theme
THEME = "/home/noelle/Dropbox/Linux/Websites/she-builds-with-code/v2_pelican/content/theme/shebuildswithcodetheme"
CSS_FILE = 'custom.css'
# THEME = "notmyidea"
# THEME = "simple"
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Web Development'

# PAY ATTENTION TO THIS SETTING BEFORE GOING LIVE
DELETE_OUTPUT_DIRECTORY = True