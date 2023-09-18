#写一个python程序，判断一个输入的字符串s，是否包含由两个或两个以上连续出现的相同字符组成的字符串。例如，abccccda中就包含cccc这四个连续字符c组成的字符串。
def repeat(s):
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i >= 2:
            return True
        i = j
    return False

s = input("请输入一个字符串: ")
if repeat(s):
    print(f"字符串 '{s}' 中包含由两个或两个以上连续出现的相同字符组成的字符串。")
else:
    print(f"字符串 '{s}' 中没有包含由两个或两个以上连续出现的相同字符组成的字符串。")

