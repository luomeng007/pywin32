# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/29 17:26
software: PyCharm

Description:
"""
import win32gui
import win32con


class Win32:
    @staticmethod
    def tutorial():
        handle = win32gui.GetForegroundWindow()
        # close window
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()