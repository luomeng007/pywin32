# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/29 17:11
software: PyCharm

Description:
"""
import win32gui


# method 1
class Win32:
    @staticmethod
    def tutorial():
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        print(hWndList)
        for hwnd in hWndList:
            title = win32gui.GetWindowText(hwnd)
            print(title)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()


# method 2:
class Win32:
    @staticmethod
    def tutorial():
        hWndList = []
        win32gui.EnumWindows(Win32.hwnd, hWndList)
        print(hWndList)

    @staticmethod
    def hwnd(handle, params):
        return params.append(handle)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()
