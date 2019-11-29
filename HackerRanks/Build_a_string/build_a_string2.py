
#26  B-A = 1 yep
A_0= 4 
B_0 = 5
S_0 = "aabaacaba"

#42 B-A = 1 yep
A_1= 8 
B_1= 9
S_1= "bacbacacb"

#20 B-A = 1 yep
A_2= 2 
B_2 = 3
S_2 = 'caaahqcqes'

#10 B-A = 2 Nop
A_3 = 1 
B_3 = 3
S_3 = 'acbbqbbqbb'

#18 B-A = 2 yep 
A_4 = 2 
B_4 = 4
S_4 = 'cbabecbahe'

# 22 B-A = 2 yep
A_5 = 2 
B_5 = 4
S_5 = 'baaceacmbaaceam'

# 13  B-A = 0  yep
A_6 = 1 
B_6 = 1
S_6 = 'acabsbccbgfeaca'

# 26 B - A= 2 yep
A_7 = 2 
B_7 = 4
S_7 = 'acabccadeljadel'
#20  23
A_8 = 1 
B_8 = 2
S_8 = 'cbaasgcbiikaegcbiidcbaasgcbiikaegcbiidir'
#24  31
A_9 = 1 
B_9 = 3
S_9 = 'cabcjpsdaedsasedsascabcjpsddsdaedsasedsa'
#45  46
A_10 = 2 
B_10 = 3
S_10 = 'cbacojcrojcrlidickjcjcrojcrlijcrojcrrojq'

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
    return lcs_set
    
def find_substring(rem, subs):
    subs = sorted(list(subs))
  
    if len(subs) == 1:
        ref = max(subs,key = len)

    for x in subs:
        f_loc = rem.find(x)
        if f_loc == 0:
            return len(x)
    return 0

def buildString(a, b, s):
    res = a
    if s[1] == s[0]:
        res += a 
        i = 1
    else:
        i = 0
    while i < len(s)-1:
        sub_st = s[:i+1]
        rem_st = s[i+1:]
        # if len(sub_st) > len(rem_st):
        #     cs = lcs(sub_st,rem_st)
        # if len(sub_st) < len(rem_st):
        #     cs = lcs(rem_st, sub_st)
        cs = lcs(sub_st, rem_st)
        fs = find_substring(rem_st, cs )

        if fs > 1:
            res += b
            i += fs
        else:
            res += a
            i += 1

    return res

 


print(buildString(A_0,B_0,S_0))