
#26  B-A = 1 yep 9
A_0= 4 
B_0 = 5
S_0 = "aabaacaba"

#42 B-A = 1 yep 9
A_1= 8 
B_1= 9
S_1= "bacbacacb"

#20 B-A = 1 yep 10
A_2= 2 
B_2 = 3
S_2 = 'caaahqcqes'

#10 B-A = 2 Nop 10
A_3 = 1 
B_3 = 3
S_3 = 'acbbqbbqbb'

#18 B-A = 2 yep  10
A_4 = 2 
B_4 = 4
S_4 = 'cbabecbahe'

# 22 B-A = 2 yep 15
A_5 = 2 
B_5 = 4
S_5 = 'baaceacmbaaceam'

# 13  B-A = 0  yep 15
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
#29
A_11 = 1 
B_11 = 3
S_11 = 'caacctinbnatinbnaqaacctinbnatinbnainbnatigaeifcaac'

#50
A_12 = 2 
A_12 = 4
S_12 = 'bbaakbbabaptakbbabaptafbbabbaakbbabapcqkmbbabaptak'

#50
A_13 = 2 
B_13 = 2
S_13 = 'cbbcnkbbcbnkbbcbtnkatnbebgcbnkbgbcnkbbcbnkmbndnknk'

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
    return list(lcs_set)
    
def buildString(a, b, s):
    lim = b-a
    res = 2*a
    i = 2
    for i in range(2, len(s)):
        act = s[:i]
        for j in range(i+1, len(s)):
            sub = s[i:j]
            if sub in act:
                




    # while i < len(s):
    #     rem = s[i:]
    #     sub = s[:i]
        # cs = lcs(sub, rem)
        # if len(cs) == 0:
        #     res += a
        #     i += 1
        #     continue
        
        # loc = rem.find(cs)
        # if loc == 0 and len(cs) > lim:
        #     res += b
        #     i += len(cs)
        # else:
        #     res += a
        #     i  += 1
    return res

 


print(buildString(A_0,B_0,S_0))