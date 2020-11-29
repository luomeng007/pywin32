# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/29 16:56
software: PyCharm

Description:
"""
import win32gui


class Win32:
    @staticmethod
    def getHandle():
        # get the top window handle
        handle = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(handle)
        class_name = win32gui.GetClassName(handle)
        # verify, when there are some special characteristics in title, we better to use r before string
        handle = win32gui.FindWindow(r"SunAwtFrame",
                                     r"main.py – C:\Users\15025\Desktop\连连看外挂\QQ_game_lianliankan-master\debug.py")
        print("The handle of this window is: ")
        print(handle)
        print("")
        print("The title of this window is: ")
        print(title)
        print("")
        print("The class name of this window is: ")
        print(class_name)
        print("")


if __name__ == '__main__':
    main = Win32()
    main.getHandle()
"""
The handle of this window is: 
395098

The title of this window is: 
main.py – C:\Users\15025\Desktop\连连看外挂\QQ_game_lianliankan-master\debug.py

The class name of this window is: 
SunAwtFrame
"""