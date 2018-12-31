# -*- coding: utf-8 -*-

"""
Example of NLog (for 64bit)
"""

import nlog

def RunExample():
    log_a = nlog.getLogger("logA", "c:\\tmp\\NLog.config")
    log_a.Trace("Trace A");
    log_a.Debug("Debug A");
    log_a.Info("Info A");
    log_a.Warn("Warn A");
    log_a.Error("Error A");
    log_a.Fatal("Fatal A");

if __name__ == '__main__':
    RunExample()