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


class Win32:
    @staticmethod
    def tutorial():
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        print(hWndList)
        for hwnd in hWndList:
            # only print the window which is visible
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                print(hwnd)
                print(title)
                print("")


if __name__ == '__main__':
    main = Win32()
    main.tutorial()
