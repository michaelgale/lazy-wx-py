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
# LazyPanel class

import wx

from .helpers import apply_attr, YamlDict


class LazyPanel(wx.Panel):
    def __init__(self, parent, layout_file, name=None):
        wx.Panel.__init__(self, parent)
        pname = name if name is not None else "root"
        layout = YamlDict(yml=layout_file)
        objs = {}
        sizer, objs = layout_panel(self, layout, pname, objs)
        for k, v in objs.items():
            self.__dict__[k] = v
        self.SetSizer(sizer)

    def print_widgets(self):
        for k, v in self.__dict__.items():
            print(k)

    def set_label(self, el, text):
        if el in self.__dict__:
            self.__dict__[el].SetLabel(text)

    def bind_obj(self, el, callback):
        if el in self.__dict__:
            obj = self.__dict__[el]
            # print(type(obj))
            if "Button" in str(type(obj)):
                self.Bind(wx.EVT_BUTTON, callback, obj)
            if "CheckBox" in str(type(obj)):
                self.Bind(wx.EVT_CHECKBOX, callback, obj)


def layout_panel(parent, layout, root, objs):
    elem = layout["widgets"]
    default_padding = 1
    if "box" in root:
        name = apply_attr(root, elem, "label", root)
        root_sizer = wx.StaticBoxSizer(wx.VERTICAL, parent, name)
    else:
        root_sizer = wx.BoxSizer(wx.VERTICAL)
    if root not in layout["panels"]:
        raise KeyError("panel with name %s not in panels" % (root))
    rows = layout["panels"][root]
    for r in rows:
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        if not isinstance(r, list):
            row = [r]
        else:
            row = r
        max_rows = 1
        for c in row:
            if c in layout["panels"]:
                el, objs = layout_panel(parent, layout, c, objs)
                max_rows = max(max_rows, len(c))
            else:
                label = apply_attr(c, elem, "label", c)
                padding = apply_attr(c, elem, "padding", default_padding)
                width = apply_attr(c, elem, "width", -1)
                height = apply_attr(c, elem, "height", -1)
                size = wx.Size(width, height)
                if "edit" in c:
                    el = wx.TextCtrl(parent, -1, label)
                elif "slider" in c:
                    el = wx.Slider(parent, -1, name=label)
                elif "line" in c:
                    el = wx.StaticLine(parent, -1)
                elif "button" in c:
                    el = wx.Button(parent, -1, label)
                elif "radio" in c:
                    el = wx.RadioButton(parent, -1, label)
                elif "spacer" in c:
                    el = wx.StaticText(parent, -1, " ")
                elif "checkbox" in c:
                    el = wx.CheckBox(parent, -1, label)
                elif "title" in c:
                    el = wx.StaticText(parent, -1, label)
                    title_font = el.GetFont()
                    title_size = apply_attr(
                        c, elem, "font_size", title_font.PointSize + 5
                    )
                    title_font.PointSize = title_size
                    title_font.MakeBold()
                    el.SetFont(title_font)
                elif "bold" in c:
                    el = wx.StaticText(parent, -1, label)
                    title_font = el.GetFont()
                    title_font.MakeBold()
                    el.SetFont(title_font)
                else:
                    el = wx.StaticText(parent, -1, label)
                if width > 0 or height > 0:
                    el.SetMinSize((width, height))
                if c in elem:
                    objs[c] = el
            row_sizer.Add(el, 1, wx.ALL | wx.TOP, padding)
        root_sizer.Add(row_sizer, max_rows, wx.TOP)
    return root_sizer, objs
