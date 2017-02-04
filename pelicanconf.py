#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import platform

########################### General Settings ###################################

AUTHOR = 'Abraham'
SITENAME = 'Notes on the margin'
SITESUBTITLE = u"Broad musings on narrow topics"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'English'
DELETE_OUTPUT_DIRECTORY = True


USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation
FEED_ALL_RSS = 'feeds/all.rss'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None #'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

## Blogroll
#LINKS = (
#        ('What If?', 'http://what-if.xkcd.com/'),
#         )
LINKS =()

# Social widget
SOCIAL = (('Academic Webpage', 'http://unm.edu/~abyvinod'),
        ('RSS', 'http://abyvinod.github.io/feeds/all.rss'),
        ('BitBucket', 'http://bitbucket.org/abyvinod'),
         ('LinkedIn', 'http://linkedin.com/in/abrahampvinod'),
          )
DEFAULT_PAGINATION = 10

# Do not generate the files starting with 0Private
# IGNORE_FILES = ['0PRIVATE*']
IGNORE_FILES = ['']
## I am using Status: drafts instead

# # Generate archive
# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
# CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images','stuff']

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

#'extra/custom.css', 'extra/href_scroll.js', 'extra/jquery.zoom.js']
# EXTRA_PATH_METADATA = {'extra/custom.css':{'path':'static/custom.css'},
#                     'extra/href_scroll.js':{'path':'theme/js/href_scroll.js'},
#                     'extra/jquery.zoom.js':{'path':'theme/js/jquery.zoom.js'},
#                        }
# for k in EXTRA_PATH_METADATA.keys(): # Fix backslash paths to resources if on Windows
#     EXTRA_PATH_METADATA[system_path(k)] = EXTRA_PATH_METADATA.pop(k)


###################### Exterior Services ############################
#DISQUS_SITENAME = 'beneathdata'
#DISQUS_SHORTNAME = 'beneathdata'
#DISQUS_DISPLAY_COUNTS = True
#
##GOOGLE_ANALYTICS = "UA-54524020-1"
#
#ADDTHIS_PROFILE = 'ra-5420884b27b877bf'
#ADDTHIS_DATA_TRACK_ADDRESSBAR = False


####################### Theme-Specific Settings #########################
THEME = 'pelican-bootstrap3'        #'html5-dopetrope'

# Pelican Theme-Specific Variables
BOOTSTRAP_THEME = 'cosmo'#'lumen' 'cosmo'
PYGMENTS_STYLE = 'monokai'
SHOW_ARTICLE_CATEGORY = True

SITELOGO = 'images/favicon_white.ico'
SITELOGO_SIZE = 20
FAVICON = 'images/favicon.ico'

ABOUT_ME = ""
#ABOUT_ME = "I'm a PhD student studying at the University of New Mexico. I am working on application of optimization and stochastic processes in dynamical systems. I also enjoy programming, especially coding in Python."

AVATAR = ""
#AVATAR = "/images/myphoto.png"
#BANNER = "/images/banner.png"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_CATEGORY = True
HIDE_SIDEBAR=True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
# Below commands will generate SITEURL/tags.html which will have the list of tags
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORIES_SAVE_AS = 'categories.html'
DIRECT_TEMPLATES=['index','tags','categories','archives']

############################ Plugins ######################################
PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['pelican-toc']#,'tag_cloud'"simple_footnotes", "feed_summary"]
TOC = {
    'TOC_HEADERS' : '^h[1-6]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression

    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}
#PLUGINS=['sitemap']
#
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.5,
#        'indexes': 0.5,
#        'pages': 0.5
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}
#FEED_USE_SUMMARY = True
#SUMMARY_MAX_LENGTH = 100

## Not working
#MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']
#MD_EXTENSIONS = (['toc', 'fenced_code', 'codehilite', 'extra'])
#MD_EXTENSIONS = ['toc','codehilite','extra']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']
#MATH_JAX = {'color':'blue'}
#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.toc': {},
#        #'markdown.extensions.fenced_code': {},
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        #'markdown.extensions.meta': {},
#    },
#    'output_format': 'html5',
#}

