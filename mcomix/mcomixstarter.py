#!/usr/bin/env python

"""MComix - GTK Comic Book Viewer
"""

# -------------------------------------------------------------------------
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# -------------------------------------------------------------------------

import os
import sys
import getopt
import signal
import gettext

import constants

try:
    import pkg_resources

except ImportError:
    # gettext isn't initialized yet, since pkg_resources is required to find translation files.
    # Thus, localizing these messages is pointless.
    print "The package 'pkg_resources' could not be found."
    print "You need to install the 'setuptools' package, which also includes pkg_resources."
    print "Note: On most distributions, 'distribute' supersedes 'setuptools'."
    sys.exit(1)

def install_gettext():
    """ Initialize gettext with the correct directory that contains
    MComix translations. This has to be done before any calls to gettext.gettext
    have been made to ensure all strings are actually translated. """

    # Add the sources' base directory to PATH to allow development without
    # explicitly installing the package.
    sys.path.append(constants.BASE_PATH)

    message_path = pkg_resources.resource_filename("mcomix.messages", "")
    gettext.install('mcomix', message_path, unicode=True)

install_gettext()

def print_help():
    """Print the command-line help text and exit."""
    print _('Usage:')
    print '  mcomix ' + _('[OPTION...] [PATH]')
    print _('\nView images and comic book archives.\n')
    print _('Options:')
    print _('  -h, --help              Show this help and exit.')
    print _('  -f, --fullscreen        Start the application in fullscreen mode.')
    print _('  -l, --library           Show the library on startup.')

    sys.exit(1)

# Check for PyGTK and PIL dependencies.
try:
    import pygtk
    pygtk.require('2.0')

    import gtk
    assert gtk.gtk_version >= (2, 12, 0)
    assert gtk.pygtk_version >= (2, 12, 0)

    import gobject
    gobject.threads_init()

except AssertionError:
    print _("You don't have the required versions of GTK+ and/or PyGTK installed.")
    print _('Installed GTK+ version is: %s') % \
        '.'.join([str(n) for n in gtk.gtk_version])
    print _('Required GTK+ version is: 2.12.0 or higher\n')
    print _('Installed PyGTK version is: %s') % \
        '.'.join([str(n) for n in gtk.pygtk_version])
    print _('Required PyGTK version is: 2.12.0 or higher')

    sys.exit(1)

except ImportError:
    print _('PyGTK version 2.12.0 or higher is required to run MComix.')
    print _('No version of PyGTK was found on your system.')

    sys.exit(1)

# Check PIL library
try:
    import Image
    assert Image.VERSION >= '1.1.5'

except AssertionError:
    print _("You don't have the required version of the Python Imaging"),
    print _('Library (PIL) installed.')
    print _('Installed PIL version is: %s') % Image.VERSION
    print _('Required PIL version is: 1.1.5 or higher')
    sys.exit(1)

except ImportError:
    print _('Python Imaging Library (PIL) 1.1.5 or higher is required.')
    print _('No version of the Python Imaging Library was found on your system.')

    sys.exit(1)

# Import required mcomix modules for this script.
# This should be done only after install_gettext() has been called.
import deprecated
import image_tools
import locale
import main
import icons
import preferences
import portability

def run():
    """Run the program."""

    fullscreen = False
    show_library = False
    open_path = None
    open_page = 1

    try:
        argv = portability.get_commandline_args()
        opts, args = getopt.gnu_getopt(argv[1:], 'fhld',
            ['fullscreen', 'help', 'library'])

    except getopt.GetoptError:
        print_help()

    for opt, value in opts:

        if opt in ('-h', '--help'):
            print_help()

        elif opt in ('-f', '--fullscreen'):
            fullscreen = True

        elif opt in ('-l', '--library'):
            show_library = True

    if not os.path.exists(constants.DATA_DIR):
        os.makedirs(constants.DATA_DIR, 0700)

    if not os.path.exists(constants.CONFIG_DIR):
        os.makedirs(constants.CONFIG_DIR, 0700)

    deprecated.move_files_to_xdg_dirs()
    preferences.read_preferences_file()
    icons.load_icons()

    if len(args) >= 1:
        param_path = os.path.abspath(args[0])

        if os.path.isdir(param_path):
            dir_files = os.listdir(param_path)
            dir_files.sort(locale.strcoll)

            for filename in dir_files:
                full_path = os.path.join(param_path, filename)

                if image_tools.is_image_file(full_path):
                    open_path = full_path
                    break
        else:
            open_path = param_path

    elif preferences.prefs['auto load last file']:
        open_path = preferences.prefs['path to last file']
        open_page = preferences.prefs['page of last file']

    window = main.MainWindow(fullscreen=fullscreen, show_library=show_library,
        open_path=open_path, open_page=open_page)
    deprecated.check_for_deprecated_files(window)

    signal.signal(signal.SIGTERM, lambda: gobject.idle_add(window.terminate_program))
    try:
        gtk.main()
    except KeyboardInterrupt: # Will not always work because of threading.
        window.save_and_terminate_program()

if __name__ == '__main__':
    run()

# vim: expandtab:sw=4:ts=4
