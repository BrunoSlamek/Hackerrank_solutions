"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
"""

from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())
words = []
for i in range(0,n):
    words.append(input())
for j in range(0,m):
    t = input()
    for i in range(0, n):
        if(t == words[i]):
            d[t].append(i+1)
    if(not d[t]):
        print("-1")
    else:
        print(" ".join([str(x) for x in d[t]]))

"""
* input;
10000 100
hejeahgdhjffafad
jebffggbdhjgj
ddfadeiibjejjbjdfijhdefbh
bifaeadjcjfbhicdhceg
ahgjccegjdhjajdbce
bbgbjjehdbfabc
cfigbjcaacjffdbbh
hibieibfebiij
fjjiabiafjfbdgccibcca
cdeihch
degcdgfbjabebgdfa
hcfjiiecibhfacaggfebgdbj
fhdchgbjeaa
hecibiadaijfdcdigfibcdd
c
jghbaggchjchfegg
bj
jfaaiefbehigdijd
fibhabcfhigihdj{-truncated-}

* Output;
-1
-1
-1
-1
-1
9977
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1{-truncated-}
"""
