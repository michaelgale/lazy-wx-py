import wx
import unittest

from lazywxpy import *


class TestLazyNotebook(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.frame.Show()

    def tearDown(self):
        wx.CallAfter(self.frame.Close)
        self.app.MainLoop()

    def testPanel(self):
        self.p = wx.Panel(self.frame)
        nb = LazyNotebook(self.p, "test_data.yml", "root")
        assert len(nb.__dict__) == 3
        assert "root" in nb.__dict__
        assert "settings_panel" in nb.__dict__
        assert "capacity_panel" in nb.__dict__
        assert nb.root is nb.__dict__["root"]


if __name__ == "__main__":
    unittest.main()
