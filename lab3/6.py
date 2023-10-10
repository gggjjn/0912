# 输入考试成绩
score = float(input("请输入考试成绩（百分制）: "))

# 使用 if 语句判断成绩等级
if score < 60:
    grade = "不合格"
elif 60 <= score < 75:
    grade = "合格"
elif 75 <= score < 90:
    grade = "良好"
else:
    grade = "优秀"

# 输出成绩等级
print(f"成绩等级: {grade}")
