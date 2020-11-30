# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/30 11:19
software: PyCharm

Description:
"""
import win32api


class Win32:
    @staticmethod
    def tutorial():
        low = 2
        high = 2
        # 将两个16位值连接为一个32位的值，二进制得研究研究了
        result = win32api.MAKELONG(low, high)
        print(result)


if __name__ == '__main__':
    main = Win32()
    main.tutorial()