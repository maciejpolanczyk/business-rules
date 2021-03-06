__version__ = '1.0.12'

import logging
from .engine import run_all
from .engine import get_value
from .utils import export_rule_data

# Appease pyflakes by "using" these exports
assert run_all
assert get_value
assert export_rule_data

logging.getLogger(__name__).addHandler(logging.NullHandler())
