# -*- coding: utf-8 -*-

"""
NLog for IronPython.

* Environment variable 'IRONPYTHON_HOME' is required. It is the installation location of IronPython.
* "NLog.dll" is required.
"""

__author__  = "WAKU-TAKE-A <waku-take-a@ymail.ne.jp>"
__version__ = "0.9.1.0"
__date__    = "2026/01/17"

#
# append path.
#
from pathlib import Path
from sys import path as systemPath
from System import Environment as env
IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")

if IRONPYTHON_HOME is None:
    raise Exception("Error : Set path of IRONPYTHON_HOME.")

CURRENT_DIR = Path(__file__).resolve().parent

IRONPYTHON_HOME_PATH = Path(IRONPYTHON_HOME)

IRONPYTHON_LIB = IRONPYTHON_HOME_PATH / "Lib"
IRONPYTHON_DLLS = IRONPYTHON_HOME_PATH / "DLLs"
IRONPYTHON_NLOG = IRONPYTHON_HOME_PATH / "Lib" / "nlog"

_lstPath = []
_lstPath.append(IRONPYTHON_LIB)
_lstPath.append(IRONPYTHON_DLLS)
_lstPath.append(IRONPYTHON_NLOG)

for i in _lstPath:
    if not i.exists():
        raise FileNotFoundError("Required directory not found: {0}. Please check your IRONPYTHON_HOME path.".format(i))
    systemPath.append(str(i))

#
# Import modules.
#
import clr
NLOG_DLL_PATH = CURRENT_DIR / "NLog.dll"
clr.AddReferenceToFileAndPath(str(NLOG_DLL_PATH))
import NLog

#
# Functions.
#
def getLogger(name="", config=None):
    if config is not None:
        config = str(Path(config).absolute())
        NLog.LogManager.LoadConfiguration(config)
    return NLog.LogManager.GetLogger(name)

