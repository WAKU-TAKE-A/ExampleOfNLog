# -*- coding: utf-8 -*-

"""
NLog for IronPython (.NET 8.0)
"""

__author__  = "WAKU-TAKE-A <waku-take-a@ymail.ne.jp>"
__version__ = "0.9.2.0"
__date__    = "2026/01/21"

#
# append path.
#
from pathlib import Path
from sys import path as systemPath
from System import Environment as env

DOTNET_SHARED = sorted(Path(r"C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App").glob("8.0.*"))[-1]
IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")

if IRONPYTHON_HOME is None:
    raise Exception("Error : Set path of IRONPYTHON_HOME.")

CURRENT_DIR = Path(__file__).resolve().parent
IRONPYTHON_HOME_PATH = Path(IRONPYTHON_HOME)

_lstPath = [
    DOTNET_SHARED,
    CURRENT_DIR,
    IRONPYTHON_HOME_PATH / "Lib",
    IRONPYTHON_HOME_PATH / "DLLs"
]

for i in _lstPath:
    if not i.exists():
        raise FileNotFoundError("Required directory not found: {0}".format(i))
    if str(i) not in systemPath:
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

