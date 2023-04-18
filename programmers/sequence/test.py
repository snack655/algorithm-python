list = ["ㅁ", "ㄴ", "ㄹ"]

print(list.index("ㅁ"))
try:
    list.index("ㄷ")
except ValueError:
    print("에러")