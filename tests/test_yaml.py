import wx

from lazywxpy.helpers import YamlDict


def test_read_dict():
    d = YamlDict(yml="test_data.yml")
    assert isinstance(d, dict)
    assert "widgets" in d
    assert "panels" in d
    assert "notebooks" in d


def test_widgets():
    d = YamlDict(yml="test_data.yml")
    assert "widgets" in d
    pd = d["widgets"]
    assert len(pd) == 10
    assert "brick_title" in pd
    assert "root" not in pd


def test_panels():
    d = YamlDict(yml="test_data.yml")
    assert "panels" in d
    pd = d["panels"]
    assert len(pd) == 7
    assert "root" in pd
    assert "settings_panel" in pd
    assert "col2" in pd


def test_notebooks():
    d = YamlDict(yml="test_data.yml")
    assert "notebooks" in d
    pd = d["notebooks"]
    assert len(pd) == 1
    assert "root" in pd
