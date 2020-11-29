# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/29 12:47
software: PyCharm

Description:
"""
import win32gui


class Tutorial:
    @staticmethod
    def mainDebug():
        handle = win32gui.GetDesktopWindow()
        # we could use this handle to deal with desktop window
        print(handle)   


if __name__ == '__main__':
    main = Tutorial()
    main.mainDebug()
"""
# 65552
"""
