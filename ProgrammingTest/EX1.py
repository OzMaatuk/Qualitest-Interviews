def sol(word: str) -> bool:
    ri = len(word)-1
    li = 0
    while (li < ri):
        if (word[li] != word[ri]):
            return False
        li+=1
        ri-=1
    return True

x = [
    "12345",
    "aba", 
    "abba",
    "12221",
    "12121",
    "22222",
    "abcdefghijklmnop",
    "abcdeflmnop",
    "abcdefghijklmnopabcdefghijklmnop",
    "abcdedcba",
    ]
for i in x:
    print(i, sol(i))