import wx
import unittest

from lazywxpy import *


class TestLazyPanel(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frame = wx.Frame(None)
        self.frame.Show()

    def tearDown(self):
        wx.CallAfter(self.frame.Close)
        self.app.MainLoop()

    def testPanel(self):
        self.p = wx.Panel(self.frame)
        panel = LazyPanel(self.p, "test_data.yml", "col2")
        # col2 has no named widgets, so empty dict
        assert len(panel.__dict__) == 0
        assert "col_title" not in panel.__dict__

        p2 = LazyPanel(self.p, "test_data.yml", "version_panel")
        # version_panel has 3 named widgets
        assert len(p2.__dict__) == 3
        # 2 of the widgets are in sub list
        assert "version_panel_check_button" in p2.__dict__
        assert isinstance(p2.version_panel_version_title, wx._core.StaticText)
        assert "version_panel_restore_button" in p2.__dict__
        assert isinstance(p2.version_panel_restore_button, wx._core.Button)
        assert p2.__dict__["version_panel_check_button"] is p2.version_panel_check_button
        assert isinstance(p2.version_panel_check_button, wx._core.Button)

        p3 = LazyPanel(self.p, "test_data.yml", "settings_panel")
        # settings_panel has 2 named widgets, both inherited
        assert "col1_box_alc_checkbox" in p3.__dict__
        assert "col3_button_ir" in p3.__dict__
        assert isinstance(p3.col1_box_alc_checkbox, wx._core.CheckBox)
        assert isinstance(p3.col3_button_ir, wx._core.Button)


if __name__ == "__main__":
    unittest.main()
