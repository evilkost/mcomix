# -*- coding: utf-8 -*-
"""constants.py - Miscellaneous constants."""

import gtk
import gc
import re
import tools
import os
import sys
import gettext
_ = gettext.gettext

VERSION = '0.90'

HOME_DIR = tools.get_home_directory()
CONFIG_DIR = tools.get_config_directory()
DATA_DIR = tools.get_data_directory()

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
THUMBNAIL_PATH = os.path.join(HOME_DIR, '.thumbnails/normal')
LIBRARY_DATABASE_PATH = os.path.join(DATA_DIR, 'library.db')
LIBRARY_COVERS_PATH = os.path.join(DATA_DIR, 'library_covers')

BOOKMARK_PICKLE_PATH = os.path.join(DATA_DIR, 'bookmarks.pickle')
PREFERENCE_PICKLE_PATH = os.path.join(DATA_DIR, 'preferences.pickle')
FILEINFO_PICKLE_PATH = os.path.join(DATA_DIR, 'file.pickle')
CRASH_PICKLE_PATH = os.path.join(DATA_DIR, 'crash.pickle')

ZOOM_MODE_BEST, ZOOM_MODE_WIDTH, ZOOM_MODE_HEIGHT, ZOOM_MODE_MANUAL = range(4)
ZIP, RAR, TAR, GZIP, BZIP2, PDF = range(6)
NORMAL_CURSOR, GRAB_CURSOR, WAIT_CURSOR = range(3)
LIBRARY_DRAG_EXTERNAL_ID, LIBRARY_DRAG_BOOK_ID, LIBRARY_DRAG_COLLECTION_ID = range(3)

RESPONSE_SORT_DESCENDING = 1
RESPONSE_SORT_ASCENDING = 2
RESPONSE_REVERT_TO_DEFAULT = 3
RESPONSE_REMOVE = 4
RESPONSE_IMPORT = 5
RESPONSE_ACCEPT_CHANGES = 6
RESPONSE_SAVE_AS = 7

ARCHIVE_DESCRIPTIONS = {
                        ZIP:   _('ZIP archive'),
                        TAR:   _('Tar archive'),
                        GZIP:  _('Gzip compressed tar archive'),
                        BZIP2: _('Bzip2 compressed tar archive'),
                        RAR:   _('RAR archive')
                       }

SUPPORTED_IMAGE_REGEX = re.compile(r'\.(jpg|jpeg|png|gif|tif|tiff|bmp|ppm|pgm|pbm)\s*$', re.I)
SUPPORTED_ARCHIVE_REGEX = re.compile(r'\.(cbz|cbr|cbt)\s*$', re.I)

_missing_icon_dialog = gtk.Dialog(None,None,0,None)
_missing_icon_pixbuf = _missing_icon_dialog.render_icon(gtk.STOCK_MISSING_IMAGE, gtk.ICON_SIZE_LARGE_TOOLBAR)
MISSING_IMAGE_ICON = _missing_icon_pixbuf.scale_simple( 128, 128, gtk.gdk.INTERP_TILES )

if sys.version_info[:3] >= (2, 5, 0):
    RUN_GARBAGE_COLLECTOR = gc.collect(0)
else:
    RUN_GARBAGE_COLLECTOR = gc.collect()

CREDITS = (
            ('Louis Casillas', _('Lead developer of MComix')),
            ('Pontus Ekberg', _('Original vision/developer of Comix')),
            ('Emfox Zhou', _('Simplified Chinese translation')),
            ('Xie Yanbo', _('Simplified Chinese translation')),
            ('Manuel Quiñones', _('Spanish translation')),
            ('Marcelo Góes', _('Brazilian Portuguese translation')),
            ('Christoph Wolk', _('German translation and Nautilus thumbnailer')),
            ('Chris Leick', _('German translation')),
            ('Raimondo Giammanco', _('Italian translation')),
            ('GhePeU', _('Italian translation')),
            ('Arthur Nieuwland', _('Dutch translation')),
            ('Achraf Cherti', _('French translation')),              
            ('Benoît H.', _('French translation')),
            ('Kamil Leduchowski', _('Polish translatin')),
            ('Darek Jakoniuk', _('Polish translation')),
            ('Paul Chatzidimitriou', _('Greek translation')),
            ('Carles Escrig Royo', _('Catalan translation')),
            ('Hsin-Lin Cheng', _('Traditional Chinese translation')),
            ('Wayne Su', _('Traditional Chinese translation')),
            ('Mamoru Tasaka', _('Japanese translation')),
            ('Ernő Drabik', _('Hungarian translation')),
            ('Artyom Smirnov', _('Russian translation')),
            ('Adrian C.', _('Croatian translation')),
            ('김민기', _('Korean translation')),
            ('Maryam Sanaat', _('Persian translation')),
            ('Andhika Padmawan', _('Indonesian translation')),
            ('Jan Nekvasil', _('Czech translation')),
            ('Олександр Заяц', _('Ukrainian translation')),
            ('Roxerio Roxo Carrillo', _('Galician translation')),
            ('Victor Castillejo', _('Icon design'))
          )