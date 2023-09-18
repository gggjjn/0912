#写一个python程序，打印“数据科学与工程导论”，并用print(chr(0x2605))语句打印的星星包围起来
def star(text):
    star = chr(0x2605)
    border = star * (len(text) + 4)
    print(border)
    print(f"{star} {text} {star}")
    print(border)
course = "数据科学与工程导论"
star(course)
