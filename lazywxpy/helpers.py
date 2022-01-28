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
# Helper functions

from metayaml import read


def apply_attr(key, d, attr, default):
    v = default
    if key in d:
        if attr in d[key]:
            v = d[key][attr]
    return v


class YamlDict(dict):
    """A deserialization of a YAML file for . and [] access"""

    def __convert(self, s, **kwargs):
        if not isinstance(s, str):
            return s
        if s.isdecimal():
            return int(s)
        if "." in s:
            fs = s.replace(".", "")
            if fs.isdecimal():
                return float(s)
        return s

    def __init__(self, yml=None, *, obj=None, baseunit="mm", **kwargs):
        """Given a YAML file that's a toplevel list or dict,
        this turns it into nested Params all the way down.

        The other args and kwargs are for internal use with recursion.
        """

        self.__dict__ = self
        if yml is not None:
            if isinstance(yml, list):
                obj = read(yml)
            else:
                obj = read([yml])
            kwargs = obj

        for k, v in list(obj.items()):
            if isinstance(v, str):
                obj[k] = self.__convert(v, **kwargs)

            if isinstance(v, dict):
                obj[k] = YamlDict(obj=v, **kwargs)

        self.update(obj)
