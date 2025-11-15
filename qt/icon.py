# SPDX-FileCopyrightText: © 2012-2022 Germar Reitze
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This file is part of the program "Back In Time" which is released under GNU
# General Public License v2 (GPLv2). See LICENSES directory or go to
# <https://spdx.org/licenses/GPL-2.0-or-later.html>.

"""Rudimentary icon caching.
Will be refactored soon."""

from PyQt6.QtGui import QIcon
import logger

# logger.debug("Checking if the current icon theme contains the BIT icon...")

# If the current icon theme does not contain the "document-save" icon
# try to use another well-known icon theme (if it is installed).
# NOTE: Icon theme names are case sensitive
themes_to_try = (
    "breeze",
    "Adwaita",
    "Yaru",
    "elementary",
    "Mint-Y",
    "mate",
    "gnome",
    "oxygen",
)

ICON_SYMBOLIC_TO_CHECK = "document-save-symbolic"
ICON_TO_CHECK = "document-save"

bit_icon = QIcon.fromTheme(ICON_SYMBOLIC_TO_CHECK)

if bit_icon.isNull():
    logger.debug(f'Icon "{ICON_SYMBOLIC_TO_CHECK}" not found, trying fallback...')
    bit_icon = QIcon.fromTheme(ICON_TO_CHECK)

for theme in themes_to_try:
    # Check if the current icon theme provides the BIT icon
    # (otherwise the icon theme is not fully or correctly installed)
    # and use this icon theme for all icons.
    if not bit_icon.isNull():
        logger.debug(
            f'Icon "{ICON_SYMBOLIC_TO_CHECK}" or "{ICON_TO_CHECK}" found in '
            "installed icon theme: {QIcon.themeName()}"
        )
        break

    # Try next icon theme (activate it)...
    QIcon.setThemeName(theme)
    logger.debug(
        f'Probing icon theme: "{theme}" ' f'(activated as "{QIcon.themeName()}")'
    )

if bit_icon.isNull():
    logger.error(
        "No supported icon theme installed (missing icons). "
        "Please consult the project website for instructions on how to fix this."
    )

# NOTE: Please prefer choosing icons from the freedesktop.org specifications
#       to improve the chance that the icon is available and each installed
#       icon theme:
#       https://specifications.freedesktop.org/icon-naming/latest/
#
# If there is chance that an icon may not always be available use
# the second argument of QIcon.fromTheme() to provide a fallback
# icon from the freedesktop.org specification.

# TODO: If we knew for sure that the global var "qapp" exists then
#       we could use a built-in "standard" Qt icon as fallback if the theme
#       does not provide the icon.
#       => wait for icon.py refactoring then improve this:
#       qapp.style().standardIcon(QStyle.SP_DialogSaveButton)
BIT_LOGO = QIcon.fromTheme("backintime")

# Loading depends on dark/light mode and is managed by systrayicon.py.
BIT_LOGO_SYMBOLIC = "backintime-symbolic"

# Main toolbar
TAKE_SNAPSHOT = QIcon.fromTheme(
    "document-save-symbolic",
    QIcon.fromTheme(
        "document-save",
    ),
)
PAUSE = QIcon.fromTheme(
    "media-playback-pause-symbolic",
    QIcon.fromTheme(
        "media-playback-pause",
    ),
)
RESUME = QIcon.fromTheme(
    "media-playback-start-symbolic",
    QIcon.fromTheme(
        "media-playback-start",
    ),
)
STOP = QIcon.fromTheme(
    "media-playback-stop-symbolic",
    QIcon.fromTheme(
        "media-playback-stop",
    ),
)
REFRESH = QIcon.fromTheme(
    "view-refresh-symbolic",
    QIcon.fromTheme(
        "view-refresh",
    ),
)
REFRESH_SNAPSHOT = REFRESH
SNAPSHOT_NAME = QIcon.fromTheme(
    "document-edit-symbolic",
    QIcon.fromTheme(
        "document-edit",
        QIcon.fromTheme(
            "text-editor-symbolic",  # for MATE
            QIcon.fromTheme(
                "accessories-text-editor",  # for GNOME
            ),
        ),
    ),
)
EDIT_USER_CALLBACK = SNAPSHOT_NAME
REMOVE_SNAPSHOT = QIcon.fromTheme(
    "edit-delete-symbolic",
    QIcon.fromTheme(
        "edit-delete",
    ),
)
VIEW_SNAPSHOT_LOG = QIcon.fromTheme(
    "document-open-symbolic",
    QIcon.fromTheme(
        "document-open",
    ),
)
VIEW_LAST_LOG = QIcon.fromTheme(
    "document-open-recent-symbolic",
    QIcon.fromTheme(
        "document-open-recent",
    ),
)
SETTINGS = QIcon.fromTheme(
    "preferences-system-symbolic",
    QIcon.fromTheme(
        "preferences-system",
    ),
)
SHUTDOWN = QIcon.fromTheme(
    "system-shutdown-symbolic",
    QIcon.fromTheme(
        "system-shutdown",
    ),
)
EXIT = QIcon.fromTheme(
    "application-exit-symbolic",
    QIcon.fromTheme(
        "application-exit",
    ),
)

# Help menu
HELP = QIcon.fromTheme(
    "help-browser-symbolic",
    QIcon.fromTheme(
        "help-browser",
        QIcon.fromTheme(
            "help-contents",
        ),
    ),
)
WEBSITE = QIcon.fromTheme(
    "go-home-symbolic",
    QIcon.fromTheme(
        "go-home",
    ),
)
CHANGELOG = QIcon.fromTheme(
    "format-justify-fill-symbolic",
    QIcon.fromTheme(
        "format-justify-fill",
    ),
)
FAQ = QIcon.fromTheme(
    "help-faq-symbolic",
    QIcon.fromTheme(
        "help-faq",
        QIcon.fromTheme(
            "help-hint",
        ),
    ),
)
QUESTION = QIcon.fromTheme(
    "dialog-question-symbolic",
    QIcon.fromTheme(
        "dialog-question",
    ),
)
BUG = QIcon.fromTheme(
    "dialog-error-symbolic",
    QIcon.fromTheme(
        "dialog-error",
    ),
)
ABOUT = QIcon.fromTheme(
    "help-about-symbolic",
    QIcon.fromTheme(
        "help-about",
    ),
)

# Files toolbar
UP = QIcon.fromTheme(
    "go-up-symbolic",
    QIcon.fromTheme(
        "go-up",
    ),
)
SHOW_HIDDEN = QIcon.fromTheme(
    "view-reveal-symbolic",
    QIcon.fromTheme(
        "view-visible",  # for Breeze and Oxygen (see #1159)
        QIcon.fromTheme(
            "show-hidden-symbolic",  # for MATE (see #507)
            QIcon.fromTheme(
                "show-hidden",  # for GNOME (see #507)
            ),
        ),
    ),
)
RESTORE = QIcon.fromTheme(
    "edit-undo-symbolic",
    QIcon.fromTheme(
        "edit-undo",
    ),
)
RESTORE_TO = QIcon.fromTheme(
    "document-revert-symbolic",
    QIcon.fromTheme(
        "document-revert",
    ),
)
SNAPSHOTS = QIcon.fromTheme(
    "view-list-symbolic",
    QIcon.fromTheme(
        "view-list-details",  # for Breeze and Oxygen
        QIcon.fromTheme(
            "system-file-manager",  # for GNOME
        ),
    ),
)

# Snapshot dialog
DIFF_OPTIONS = SETTINGS
DELETE_FILE = REMOVE_SNAPSHOT
SELECT_ALL = QIcon.fromTheme(
    "edit-select-all-symbolic",
    QIcon.fromTheme(
        "edit-select-all",
    ),
)

# Restore dialog
RESTORE_DIALOG = VIEW_SNAPSHOT_LOG

# Settings dialog
SETTINGS_DIALOG = SETTINGS
PROFILE_EDIT = SNAPSHOT_NAME
ADD = QIcon.fromTheme(
    "list-add-symbolic",
    QIcon.fromTheme(
        "list-add",
    ),
)
REMOVE = QIcon.fromTheme(
    "list-remove-symbolic",
    QIcon.fromTheme(
        "list-remove",
    ),
)
FOLDER = QIcon.fromTheme(
    "folder-symbolic",
    QIcon.fromTheme(
        "folder",
    ),
)
FILE = QIcon.fromTheme(
    "document-open-symbolic",
    QIcon.fromTheme(
        "document-open",
    ),
)
EXCLUDE = QIcon.fromTheme(
    "edit-delete-symbolic",
    QIcon.fromTheme(
        "edit-delete",
    ),
)
DEFAULT_EXCLUDE = QIcon.fromTheme(
    "emblem-important-symbolic",
    QIcon.fromTheme(
        "emblem-important",
    ),
)
INVALID_EXCLUDE = QIcon.fromTheme(
    "face-surprise-symbolic",
    QIcon.fromTheme(
        "face-surprise",
    ),
)
ENCRYPT = QIcon.fromTheme(
    "security-high-symbolic",
    QIcon.fromTheme(
        "security-high",
    ),
)
LANGUAGE = QIcon.fromTheme(
    "preferences-desktop-locale-symbolic",
    QIcon.fromTheme(
        "preferences-desktop-locale",
    ),
)
