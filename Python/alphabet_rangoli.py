"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a,
and the boundary has the  alphabet letter (in alphabetical order).
"""

def print_rangoli(r):
    s = 'abcdefghijklmnopqrstuvwxyz'
    pat = [s[r-i-1:r][::-1] + s[r-i-1:r][1:] for i in range(r)]
    pat = pat + pat[:-1][::-1]
    for i in range(len(pat)):
        print(*pat[i].center((r*2)-1,'-'), sep='-')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

