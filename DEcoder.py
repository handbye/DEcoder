# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilenames
from base64 import b64encode, b64decode, b32encode, b32decode
from urllib.parse import quote, unquote
from requests.utils import requote_uri
from hashlib import md5
from pathlib import Path

window = tk.Tk()
window.title('DEcoder')
window.geometry('800x650')

# Base64/32编码解码
# 窗体名称
b64Text = tk.Label(window, text='Base64/32编码解码:', font=('微软雅黑', 16))
b64Text.place(x=10, y=10, anchor='nw')
# 左侧输入输出框
b64_input = tk.Text(window, height=8, width=40)
b64_input.place(x=10, y=40, anchor='nw')
# 右侧输入输出框
b64_output = tk.Text(window, height=8, width=40)
b64_output.place(x=500, y=40, anchor='nw')


# base64编码函数
def b64_encode():
    result = b64_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = b64encode(result.encode(var_base_type.get()))
    b64_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    b64_output.insert('end', result)


# base64解码函数
def b64_decode():
    result = b64_output.get("0.0", "end")  # 从0行0列获取输入值直到结束
    result = b64decode(result.strip())
    result = result.decode(var_base_type.get())
    b64_input.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    b64_input.insert('end', result)


# base32编码函数
def b32_encode():
    result = b64_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = b32encode(result.encode(var_base_type.get()))
    b64_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    b64_output.insert('end', result)


# base32解码函数
def b32_decode():
    result = b64_output.get("0.0", "end")  # 从0行0列获取输入值直到结束
    result = b32decode(result.strip())
    result = result.decode(var_base_type.get())
    b64_input.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    b64_input.insert('end', result)


def base_select_encode():
    if var_base_num.get() == "base32":
        return b32_encode()
    if var_base_num.get() == "base64":
        return b64_encode()


def base_select_decode():
    if var_base_num.get() == "base32":
        return b32_decode()
    if var_base_num.get() == "base64":
        return b64_decode()


# 选择按钮
var_base_num = tk.StringVar(None, 'base64')  # 设置默认值为base64
base_num1 = tk.Radiobutton(window, text='base32', variable=var_base_num, value='base32')
base_num1.place(x=310, y=65, anchor='nw')
base_num2 = tk.Radiobutton(window, text='base64', variable=var_base_num, value='base64')
base_num2.place(x=410, y=65, anchor='nw')

# 选择按钮
var_base_type = tk.StringVar(None, 'utf-8')  # 设置默认值为utf-8
base_type1 = tk.Radiobutton(window, text='gbk', variable=var_base_type, value='gbk')
base_type1.place(x=310, y=40, anchor='nw')
base_type2 = tk.Radiobutton(window, text='utf-8', variable=var_base_type, value='utf-8')
base_type2.place(x=410, y=40, anchor='nw')

# 编码解码按钮
b1 = tk.Button(window, text='编码 -->', width=10, height=1, command=base_select_encode)
b2 = tk.Button(window, text='<-- 解码', width=10, height=1, command=base_select_decode)
b1.place(x=335, y=95, anchor='nw')
b2.place(x=335, y=120, anchor='nw')

# URL编码解码
# 窗体名称
urlText = tk.Label(window, text='URL编码解码:', font=('微软雅黑', 16))
urlText.place(x=10, y=160, anchor='nw')
# 左侧输入输出框
url_input = tk.Text(window, height=6, width=40)
url_input.place(x=10, y=190, anchor='nw')
# 右侧输入输出框
url_output = tk.Text(window, height=6, width=40)
url_output.place(x=500, y=190, anchor='nw')


def url_all_encode():
    result = url_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = quote(result)
    url_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    url_output.insert('end', result)


def url_key_encode():
    result = url_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = requote_uri(result)
    url_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    url_output.insert('end', result)


def url_decode():
    result = url_output.get("0.0", "end")  # 从0行0列获取输入值直到结束
    result = unquote(result.strip())
    url_input.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    url_input.insert('end', result)


def url_select_encode():
    if var_url_type.get() == "all":
        return url_all_encode()
    if var_url_type.get() == "key":
        return url_key_encode()


# 选择按钮
var_url_type = tk.StringVar(None, 'key')  # 设置默认值为全编码
url_type1 = tk.Radiobutton(window, text='全编码', variable=var_url_type, value='all')
url_type1.place(x=310, y=190, anchor='nw')
url_type2 = tk.Radiobutton(window, text='关键词编码', variable=var_url_type, value='key')
url_type2.place(x=400, y=190, anchor='nw')

# 编码解码按钮
c1 = tk.Button(window, text='编码 -->', width=10, height=1, command=url_select_encode)
c2 = tk.Button(window, text='< --解码', width=10, height=1, command=url_decode)
c1.place(x=335, y=215, anchor='nw')
c2.place(x=335, y=240, anchor='nw')

# 字符串与HEX互转
# 窗体名称
unicodeText = tk.Label(window, text='字符串与hex互转:', font=('微软雅黑', 16))
unicodeText.place(x=10, y=280, anchor='nw')
# 左侧输入输出框
unicode_input = tk.Text(window, height=3.5, width=40)
unicode_input.place(x=10, y=310, anchor='nw')
# 右侧输入输出框
unicode_output = tk.Text(window, height=3.5, width=40)
unicode_output.place(x=500, y=310, anchor='nw')


def unicode_encode():
    result = unicode_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = ''.join([hex(ord(i)) for i in result.strip()])
    unicode_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    unicode_output.insert('end', result)


def unicoce_decode():
    result = unicode_output.get("0.0", "end")  # 从0行0列获取输入值直到结束
    result = result.split('0x')
    result.remove('')
    result = ''.join([chr(int(i, 16)) for i in result])
    unicode_input.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    unicode_input.insert('end', result)


d1 = tk.Button(window, text='str to hex -->', width=10, height=0, command=unicode_encode)
d2 = tk.Button(window, text='<-- hex to str', width=10, height=0, command=unicoce_decode)
d1.place(x=335, y=310, anchor='nw')
d2.place(x=335, y=340, anchor='nw')

# ASCII与字符串互转
# 窗体名称
ascText = tk.Label(window, text='字符串与ASCII互转:', font=('微软雅黑', 16))
ascText.place(x=10, y=380, anchor='nw')
# 左侧输入输出框
asc_input = tk.Text(window, height=3.5, width=40)
asc_input.place(x=10, y=410, anchor='nw')
# 右侧输入输出框
asc_output = tk.Text(window, height=3.5, width=40)
asc_output.place(x=500, y=410, anchor='nw')


def asc_encode():
    result = asc_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = ' '.join([str(ord(i)) for i in result.strip()])
    asc_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    asc_output.insert('end', result)


def asc_decode():  # 目前仅支持连续的中文和英文ascii转字符串
    tkinter.messagebox.showinfo(title='提示', message='目前仅支持连续的中文或英文ascii转字符串,否则会出现顺序错乱.')
    result = asc_output.get("0.0", "end").strip()
    ch_list = []
    en_list = []
    result_new = result.split(' ')
    for i in result_new:
        if int(i) > 127:
            ch_list.append(i)
        else:
            en_list.append(i)
    ch_asc = (ch_list[i:i + 2] for i in range(0, len(ch_list), 2))
    result_out = ''
    for y in ch_asc:
        for s in y:
            result_out += chr(int(s))
    for z in en_list:
        result_out += chr(int(z))
    asc_input.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    asc_input.insert('end', result_out)


e1 = tk.Button(window, text='str to ASCII -->', width=10, height=0, command=asc_encode)
e2 = tk.Button(window, text='<-- ASCII to str', width=10, height=0, command=asc_decode)
e1.place(x=335, y=410, anchor='nw')
e2.place(x=335, y=440, anchor='nw')


# md5加密
# 窗体名称
md5Text = tk.Label(window, text='md5 hash 计算:', font=('微软雅黑', 16))
md5Text.place(x=10, y=480, anchor='nw')
# 左侧输入输出框
md5_input = tk.Text(window, height=2, width=40)
md5_input.place(x=10, y=510, anchor='nw')


def select_file():
    md5_text.delete("0.0", "end")
    filenames = askopenfilenames()
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            string_filename += str(filenames[i])+"\n"
        md5_text.insert("end", string_filename)
    else:
        md5_text.insert("end", "您没有选择任何文件")


# 文件选择框
md5_text = tk.Text(window, height=4, width=40)
md5_text.place(x=10, y=560, anchor='nw')
md5_text.insert('end', '可以选择单个文件或多个文件!')
# 文件选择按钮
md5_file_buttom = tk.Button(window, text='选择文件', width=5, height=0, command=select_file)
md5_file_buttom.place(x=300, y=600, anchor='nw')
# 右侧输出框
md5_output = tk.Text(window, height=6, width=40)
md5_output.place(x=500, y=530, anchor='nw')

# 选择按钮
var_md5_type = tk.StringVar(None, '32')  # 设置默认值为全编码
md5_type1 = tk.Radiobutton(window, text='md5(16)', variable=var_md5_type, value='16')
md5_type1.place(x=310, y=510, anchor='nw')
md5_type2 = tk.Radiobutton(window, text='md5(32)', variable=var_md5_type, value='32')
md5_type2.place(x=400, y=510, anchor='nw')


def md5_32():
    result = md5_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = md5(result.encode('utf-8')).hexdigest()
    md5_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    md5_output.insert('end', result.strip())


def md5_16():
    result = md5_input.get("0.0", "end")[:-1]  # 从0行0列获取输入值直到结束
    result = md5(result.encode('utf-8')).hexdigest()[8:-8]
    md5_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    md5_output.insert('end', result.strip())


def md5_select():
    if var_md5_type.get() == '16':
        return md5_16()
    if var_md5_type.get() == '32':
        return md5_32()


def md5_file_32():
    fnames = md5_text.get("0.0", "end").strip()
    fnames = fnames.split('\n')
    result = ''
    for fname in fnames:
        try:
            result += md5(Path(fname).read_bytes()).hexdigest()
            result += '\n'
        except Exception as e:
            tkinter.messagebox.showerror(title='错误', message='未选择文件或打开文件错误.')
    md5_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    md5_output.insert('end', result.strip())


def md5_file_16():
    fnames = md5_text.get("0.0", "end").strip()
    fnames = fnames.split('\n')
    result = ''
    for fname in fnames:
        try:
            result += md5(Path(fname).read_bytes()).hexdigest()[8:-8]
            result += '\n'
        except:
            tkinter.messagebox.showerror(title='错误', message='未选择文件或打开文件错误.')

    md5_output.delete("0.0", "end")  # 每次输出结果前先清空文本框内的内容
    md5_output.insert('end', result.strip())


def md5_select_file():
    if var_md5_type.get() == '16':
        return md5_file_16()
    if var_md5_type.get() == '32':
        return md5_file_32()


f1 = tk.Button(window, text='文本hash -->', width=10, height=0, command=md5_select)
f1.place(x=335, y=540, anchor='nw')
f2 = tk.Button(window, text='文件hash -->', width=10, height=0, command=md5_select_file)
f2.place(x=335, y=570, anchor='nw')

# 主窗口循环显示
window.mainloop()
