#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
        ('What If?', 'http://what-if.xkcd.com/'),
         )

# Social widget
SOCIAL = (('BitBucket', 'http://bitbucket.org/abyvinod'),
         ('LinkedIn', 'http://linkedin.com/in/abrahampvinod'),
          ('Academic Webpage', 'http://unm.edu/~abyvinod'),
          )

DEFAULT_PAGINATION = 10

# Do not generate these files
IGNORE_FILES = ['toDo.md']
# ARTICLE_URL = '{category}/{slug}/'
# ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'
# TAG_URL = 'tags/{slug}.html'
# TAG_SAVE_AS = 'tags/{slug}.html'
# TAGS_URL = 'tags.html'

# # Generate archive
# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
# CUSTOM_CSS = 'static/custom.css'
# STATIC_PATHS = ['images', 'extra/custom.css', 'extra/href_scroll.js', 'extra/jquery.zoom.js']
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
THEME = 'pelican-bootstrap3'#'html5-dopetrope'

# Pelican Theme-Specific Variables
BOOTSTRAP_THEME = 'sandstone'#'lumen' 'cosmo'
SHOW_ARTICLE_CATEGORY = True

#SITELOGO = 'images/logo.png'
#SITELOGO_SIZE = 32
#FAVICON = 'images/favicon.png'

ABOUT_ME = "I'm a PhD student studying at the University of New Mexico. I am working on application of optimization and stochastic processes in dynamical systems. I also enjoy programming, especially coding in Python."

AVATAR = "/images/myphoto.png"

#BANNER = "/images/banner.png"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

PYGMENTS_STYLE = 'monokai'

############################ Plugins ######################################
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['simple_footnotes', 'extract_toc', 'feed_summary']
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']

