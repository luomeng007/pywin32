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
import time
import win32con


class Win32:
    @staticmethod
    def tutorial():
        handle = win32gui.GetForegroundWindow()
        win32gui.CloseWindow(handle)
        time.sleep(1)
        # maximize current window
        win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()