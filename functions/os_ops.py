import os
import subprocess as sp


def open_vscode():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Visual Studio Code\" to activate'])


def open_discord():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Discord\" to activate'])


def open_cmd():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Terminal\" to activate'])


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Calculator\" to activate'])