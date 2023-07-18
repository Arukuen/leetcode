# Thought that BST style might work

# def longestCommonPrefix(strs: list[str]) -> str:
#     left = 0
#     right = min(map(lambda str: len(str), strs))
#     prev_mid = 0

#     while True:
#         mid = (left + right) // 2
#         if prev_mid == mid:
#             return strs[0][:right]
        
#         if all(map(lambda str: str[mid] == strs[0][mid], strs)):
#             left = mid
#         else:
#             right = mid

#         prev_mid = mid

def longestCommonPrefix(strs: list[str]) -> str:
    min_len = min(map(lambda str: len(str), strs))
    if min_len == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    for i in range(min_len):  
        if all(map(lambda str: str[i] == strs[0][i], strs)):
            if i+1 == min_len:
                return strs[0][:i+1]
        else:
            return strs[0][:i]


print(longestCommonPrefix(["flower","flow","flight"]))