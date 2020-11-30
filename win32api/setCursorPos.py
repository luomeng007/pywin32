# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/30 11:11
software: PyCharm

Description:
"""
import win32api


class Win32:
    @staticmethod
    def tutorial():
        position = (0, 0)
        # move curse to left top position of screen
        win32api.SetCursorPos(position)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()