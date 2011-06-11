# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue May 31 20:54:02 2011

import wx

import ConfigElements
from core.application import Application
from gui.guiconfig import HtmlRenderConfig
from core.config import FontOption, StringOption

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class HtmlRenderPanel(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: HtmlRenderPanel.__init__
		kwds["style"] = wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		self.fontLabel = wx.StaticText(self, -1, _("Font"))
		self.fontPicker = wx.FontPickerCtrl(self, -1)
		self.userStyleLabel = wx.StaticText(self, -1, _("Additional styles (CSS):"))
		self.userStyleTextBox = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE|wx.HSCROLL|wx.TE_LINEWRAP|wx.TE_WORDWRAP)

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

		self.config = HtmlRenderConfig (Application.config)

		self.LoadState()


	def __set_properties(self):
		# begin wxGlade: HtmlRenderPanel.__set_properties
		self.SetSize((415, 257))
		# end wxGlade


	def __do_layout(self):
		# begin wxGlade: HtmlRenderPanel.__do_layout
		mainSizer = wx.FlexGridSizer(1, 1, 0, 0)
		fontSizer = wx.FlexGridSizer(1, 2, 0, 0)
		fontSizer.Add(self.fontLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
		fontSizer.Add(self.fontPicker, 1, wx.EXPAND, 0)
		fontSizer.AddGrowableCol(1)
		mainSizer.Add(fontSizer, 1, wx.EXPAND, 0)
		mainSizer.Add(self.userStyleLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
		mainSizer.Add(self.userStyleTextBox, 0, wx.ALL|wx.EXPAND, 2)
		self.SetSizer(mainSizer)
		mainSizer.AddGrowableRow(2)
		mainSizer.AddGrowableCol(0)
		# end wxGlade


	def LoadState(self):
		# Шрифт для HTML-рендера
		fontOption = FontOption (self.config.fontFaceNameOption, 
				self.config.fontSizeOption, 
				self.config.fontIsBold, 
				self.config.fontIsItalic)

		self.fontEditor = ConfigElements.FontElement (fontOption, self.fontPicker)

		self.userStyle = ConfigElements.StringElement (self.config.userStyleOption, self.userStyleTextBox)


	def Save (self):
		self.fontEditor.save()
		self.userStyle.save()

		#Application.onEditorConfigChange()

# end of class HtmlRenderPanel


