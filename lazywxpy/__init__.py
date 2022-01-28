"""lazywxpy - A python package to make wxWidgets GUIs from YAML files."""

import os

# fmt: off
__project__ = 'lazywxpy'
__version__ = '0.1.0'
# fmt: on

VERSION = __project__ + "-" + __version__

script_dir = os.path.dirname(__file__)

from .lazypanel import LazyPanel
from .lazynotebook import LazyNotebook
