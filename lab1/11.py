#写一个python程序，输入一个字符串s，去掉其中所有的空格后输出。
s = input("请输入一个字符串: ")
s_without_spaces = s.replace(" ", "")
print("去掉空格后的字符串:", s_without_spaces)