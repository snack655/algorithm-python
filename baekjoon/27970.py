# sum = 0
# arr = list(input())
# for i in range(0, len(arr)):
#     if arr[i] == "O":
        
#         sum += 2**i
# print(sum % ((10**9)+7))


print(int(input()[::-1].replace('O', '1').replace('X', '0'), 2) % 1000000007)