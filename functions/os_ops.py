import os
import subprocess as sp

def open_finder():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Finder\" to activate'])


def open_vscode():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Visual Studio Code\" to activate'])


def open_discord():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Discord\" to activate'])


def open_cmd():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Terminal\" to activate'])


def open_camera():
     sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"FaceTime\" to activate'])


def open_calculator():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Calculator\" to activate'])
    
    
def open_safari():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Safari\" to activate'])
    
    
def open_brave():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Brave\" to activate'])
    
    
def open_chrome():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Chrome\" to activate'])
    
    
def open_contacts():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Contacts\" to activate'])


def open_calendar():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Calendar\" to activate'])


def open_notes():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Notes\" to activate'])


def open_messages():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Messages\" to activate'])
    
    
def open_plans():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Plans\" to activate'])


def open_photos():
    sp.Popen(['/usr/bin/osascript', '-e', 'tell application \"Photos\" to activate'])
