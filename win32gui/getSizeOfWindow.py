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
        # this is the handle of desktop
        handle = 65552
        left, top, right, bottom = win32gui.GetWindowRect(handle)
        print(f"The left is {left}")
        print(f"The left is {top}")
        print(f"The left is {right}")
        print(f"The left is {bottom}")


if __name__ == '__main__':
    main = Win32()
    main.tutorial()
"""
The left is 0
The left is 0
The left is 1920
The left is 1200
"""