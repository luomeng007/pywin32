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


class Win32:
    @staticmethod
    def tutorial():
        handle = win32gui.GetForegroundWindow()
        # minimize current window
        win32gui.CloseWindow(handle)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()