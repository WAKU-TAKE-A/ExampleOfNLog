# -*- coding: utf-8 -*-

"""
Example of NLog (for 64bit)
"""

from pathlib import Path
import nlog

CURRENT_FILE_PATH = Path(__file__).resolve()
EXAMPLES_DIR = CURRENT_FILE_PATH.parent
CONFIG_PATH = EXAMPLES_DIR / 'NLog.config'

def run():
    print("CONFIG_PATH:")
    print(CONFIG_PATH)
    log_a = nlog.getLogger('logA', str(CONFIG_PATH))
    log_a.Trace('Trace (IPY)');
    log_a.Debug('Debug (IPY)');
    log_a.Info('Info (IPY)');
    log_a.Warn('Warn (IPY)');
    log_a.Error('Error (IPY)');
    log_a.Fatal('Fatal (IPY)');
    print("Saved the logs to the desktop.")

if __name__ == '__main__':
    run()