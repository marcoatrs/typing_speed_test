import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    ROOT_PATH = Path(sys.executable).parent
else:
    ROOT_PATH = Path(__file__).parents[2]
