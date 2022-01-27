#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os

AUTHOR = 'Yevhen Yakubovskyi'
SITENAME = "Yevhen Yakubovskyi"
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = "feeds/all.rss"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME="pelican-subtle/"
PLUGIN_PATHS=["pelican-subtle/plugins"]
PLUGINS=["pelican-subtle.plugins.assets.pelican-assets"]

#Theme specific
TAGLINE = "Software Developer"
#USER_LOGO_URL = ""
MANGLE_EMAILS = True
#GLOBAL_KEYWORDS = ("cmetcalfe", "carey", "metcalfe", "pr0ps", "pr0pscm", "blog")
FUZZY_DATES = True
DISQUS_SITENAME = "mrlutik"
DISQUS_COLLAPSED = True

# Webassets plugin
ASSET_CONFIG = (("url_expire", False),)
ASSET_DEBUG = False

MARKDOWN = {
    'extension_configs':{
        'markdown.extensions.codehilite': {"css_class": "highlight", "guess_lang": False, "linenums": True},
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}
LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'

STATIC_PATHS = ['images', "files"]
EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}



# Blogroll
SOCIAL = (
    ('GitHub', 'https://github.com/MrLutik'),
    ('Email', 'mailto:yaievgeniy@gmail.com'),
    )

# Social widget
LINKS = (

)

DEFAULT_PAGINATION = 3


RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = None

INDEX_SAVE_AS = "blog/index.html"
ARCHIVES_URL = "blog/archives.html"
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'
TAG_URL = 'blog/tags/{slug}.html'
TAG_SAVE_AS = 'blog/tags/{slug}.html'

CATEGORIES_URL = ''#'blog/categories/'
CATEGORIES_SAVE_AS = ''#'blog/categories/index.html'
CATEGORY_URL = ''#'blog/categories/{slug}.html'
CATEGORY_SAVE_AS = ''#'blog/categories/{slug}.html'

AUTHORS_URL = ''#'blog/authors/'
AUTHORS_SAVE_AS = ''#'blog/authors/index.html'
AUTHOR_URL = ''#'blog/authors/{slug}.html'
AUTHOR_SAVE_AS = ''#'blog/authors/{slug}.html'
