# lazy-wx-py

![python version](https://img.shields.io/static/v1?label=python&message=3.6%2B&color=blue&style=flat&logo=python)
![https://github.com/michaelgale/toolbox-py/blob/master/LICENSE](https://img.shields.io/badge/license-MIT-blue.svg)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>  

This package will build simple [wxPython](https://www.wxpython.org) ([wxWidgets](https://www.wxwidgets.org) python port) based GUI layouts from YAML files.  In particular it will build nested `wx.Panel` layouts and `wx.Notebook` pages from simple YAML syntax.  Furthermore, if the YAML file specifies named widgets, it will add these widgets to the their corresponding `wx.Panel` dictionaries for dotted attribute access.

## YAML File

The YAML file should have these sections:

* widgets
* panels
* notebooks

```yaml

widgets:
  checkbox_a:
    label: "Use group A"
    padding: 10
  checkbox_b:
    label: "Use group B"
    padding: 10
  apply_button:
    label: "Apply"
    width: 100
  cancel_button:
    label: "Cancel"
  column_title:
    label: "Settings"
  confirm_button:
    label: "Confirm"

panels:
  settings1:
    - checkbox_a
    - checkbox_b
  settings2:
    - apply_button
    - cancel_button
  page2:
    - column_title
    - [settings1, settings2]
    - confirm_button

notebooks:
  root:
    - page1: Info
    - page2: Settings
    - Page3: Files
```

**LazyPanel**

- `LazyPanel` class is derived from `wx.Panel`
- its constructor is passed a YAML file and named entity in `panels`

**LazyNotebook**

- `LazyNotebook` class is derived from `wx.Notebook`
- its constructor is passed a YAML file and named entity in `notebooks`


## Installation

The **toolbox** package can be installed directly from the source code:


```shell
    $ git clone https://github.com/michaelgale/lazy-wx-py.git
    $ cd lazy-wx-py
    $ python setup.py install
```

## Usage

After installation, the package can imported:

```shell
    $ python
    >>> import lazywxpy
    >>> lazywxpy.__version__
```

An example of the package can be seen below

```python
  import wx
  from lazywxpy import LazyPanel

  class MyFrame(wx.Frame):
      def __init__(self, parent, id, title):
          wx.Frame.__init__(self, parent, id, title, size=(860, 600))
          panel = LazyPanel(self, "layout.yml", "root")
          sizer = wx.BoxSizer()
          sizer.Add(panel, 1, wx.EXPAND)
          self.SetSizer(sizer)

  class MyApp(wx.App):
      def OnInit(self):
          frame = MyFrame(None, -1, "Test App")
          self.SetTopWindow(frame)
          frame.Show(True)
          return True

  def main():
      app = MyApp(redirect=False)
      app.MainLoop()
          
  if __name__ == "__main__" :
      main()          
```

## Requirements

* Python 3.6+
* jinja2 
* metayaml
* wxpython
* pytest

## References

* [wxPython](https://www.wxpython.org)
* [wxPyWiki](https://wiki.wxpython.org)
* [wxPython Classes Cheat Sheet](https://wiki.wxpython.org/wxClassesCheatSheet)

## Authors

`lazy-wx-py` was written by [Michael Gale](https://github.com/michaelgale)
