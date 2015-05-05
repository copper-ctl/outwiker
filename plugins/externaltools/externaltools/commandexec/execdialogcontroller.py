# -*- coding: UTF-8 -*-

from StringIO import StringIO

import wx

from externaltools.commandexec.commandparams import (
    TITLE_NAME,
    FORMAT_NAME,
    FORMAT_BUTTON
)


class ExecDialogController (object):
    def __init__ (self, dialog, application):
        self._dialog = dialog
        self._application = application


    def showDialog (self):
        """
        The method shows dialog and return result of the ShowModal method
        """
        self._loadState()

        result = self._dialog.ShowModal()
        if result == wx.ID_OK:
            self._saveState()

        return result


    def _loadState (self):
        pass


    def _saveState (self):
        pass


    def getResult (self):
        """
        Return tuple: (begin command, end command)
        """
        openCommand = StringIO()
        openCommand.write (u'(:exec')

        if self._dialog.title:
            openCommand.write (u' {}="{}"'.format (TITLE_NAME, self._dialog.title))

        if self._dialog.format == 1:
            openCommand.write (u' {}="{}"'.format (FORMAT_NAME, FORMAT_BUTTON))

        openCommand.write (u':)')

        closeComamnd = u'(:execend:)'

        return (openCommand.getvalue(), closeComamnd)