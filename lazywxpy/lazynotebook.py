#! /usr/bin/env python3
#
# Copyright (C) 2022  Michael Gale
# This file is part of the legocad python module.
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# LazyNotebook class

import wx

from .lazypanel import LazyPanel
from .helpers import YamlDict


class LazyNotebook(wx.Panel):
    def __init__(self, parent, layout_file, name):
        wx.Panel.__init__(self, parent)
        name = name if name is not None else "root"
        layout = YamlDict(yml=layout_file)
        pages = layout["notebooks"][name]
        notebook = wx.Notebook(self)
        for page in pages:
            page = dict(page)
            for k, v in page.items():
                name = k
                title = v
            panel = LazyPanel(notebook, layout_file, name=name)
            self.__dict__[name] = panel
            notebook.AddPage(panel, title)
        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def print_pages(self):
        for k, v in self.__dict__.items():
            if isinstance(v, (LazyPanel, wx.Panel)):
                print(k)
