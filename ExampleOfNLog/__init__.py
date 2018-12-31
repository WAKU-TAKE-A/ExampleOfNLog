# -*- coding: utf-8 -*-

"""
NLog for IronPython.

* Environment variable 'IRONPYTHON_HOME' is required. It is the installation location of IronPython.
* "NLog.dll" is required.
"""

__author__  = "Nishida Takehito <takehito.nishida@gmail.com>"
__version__ = "0.9.0.0"
__date__    = "2018/12/27"

#
# append path.
#
import os
import os.path as path
from sys import path as systemPath
from System import Environment as env
IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")

if IRONPYTHON_HOME is None:
    raise Exception("Error : Set path of IRONPYTHON_HOME.")

IRONPYTHON_LIB = path.join(IRONPYTHON_HOME, "Lib")
IRONPYTHON_DLLS = path.join(IRONPYTHON_HOME, "DLLs")
IRONPYTHON_NLOG = path.join(IRONPYTHON_HOME, "Lib\\nlog")

_lstPath = []
_lstPath.append(IRONPYTHON_LIB)
_lstPath.append(IRONPYTHON_DLLS)
_lstPath.append(IRONPYTHON_NLOG)

_checkPath = True

for i in _lstPath:
    if os.path.exists(i):
        systemPath.append(i)
    else:
        _checkPath = False
        print("There is no '" + i + "'.")

if _checkPath == False:
	raise Exception("Error occured.")

#
# Import modules.
#
import clr
clr.AddReferenceToFile("NLog.dll")
import NLog

#
# Functions.
#
def getLogger(name="", config=None):
    if config != None:
        NLog.LogManager.LoadConfiguration(config)
    return NLog.LogManager.GetLogger(name)

