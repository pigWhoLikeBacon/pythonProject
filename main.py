import ctypes
import sys
import time
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def timeAync():
    cmd('net stop w32time')
    cmd('w32tm /unregister')
    cmd('w32tm /register')
    cmd('net start w32time')
    cmd('w32tm /resync')


def cmd(order):
    print('Run command:', order)
    d = os.popen(order)
    print(d.read())
    return


if is_admin():
    while 1:
        print('Start adjust time!')
        timeAync()
        print('Sleep 60s!')
        time.sleep(60)
else:
    # Re-run the program with admin rights
    print('Need admin access')
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
