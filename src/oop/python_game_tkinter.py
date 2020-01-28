"""
使用thinter的步骤
    1. 导入tkinter模块中我们需要的东西。
    2. 创建一个顶层窗口对象并用它来承载整个GUI应用。
    3. 在顶层窗口对象上添加GUI组件。
    4. 通过代码将这些GUI组件的功能组织起来。
    5. 进入主事件循环(main loop)。
"""
import tkinter
import tkinter.messagebox

import pygame


def main():
    """
    基于tkinter模块开发GUI
    :return:
    """
    flag = True

    # 回调函数,修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello World') \
            if flag else ('blue', 'Goodbye')
        label.config(text=msg, fg=color)

    # 确认退出提醒
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("温馨提示", '确定退出吗？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x150')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello World', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到容器对象的名字，通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
