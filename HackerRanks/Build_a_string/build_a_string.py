
apd_0= 4 
cop_0 = 5
s_0 = "aabaacaba"

apd_1= 8 
cop_1= 9
s_1= "bacbacacb"

apd_2= 7890 
cop_2= 7891 
s_2= "acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh"

    
#20
apd_3= 2 
cop_3 = 3
s_3 = 'caaahqcqes'

#10
apd_4 = 1 
cop_4 = 3
s_4 = 'acbbqbbqbb'

#18
apd_5 = 2 
cop_5 = 4
s_5 = 'cbabecbahe'

    # 3

    # 15 2 4

    # baaceacmbaaceam

    # 15 1 1

    # acabsbccbgfeaca

    # 15 2 4

    # acabccadeljadel

    # 22

    # 13

    # 26



def get_substrings(s):
    subs_set = set()
    n = len(s)
    for i in range(n): 
        for x in range(i+1,n+1): 
                #subs.add(s[i:x])
                subs_set.add(s[i:x])
    subs_list = sorted(list(subs_set))
    return subs_list

def find_substring(s, subs_set):
    s_list = [s]
    ints = subs_set.intersection(set(s_list))
    if len(s) == 0:
        return 
    elif len(ints) != 0:
        return ints
    else:
        return find_substring(s[:-1], subs_set)
    
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
        subs =  get_substrings(sub_st)
        i += 1


    #     # subs_set = subs_set.union(get_substrings(sub_st,subs_set))
    #     # tot = find_substring(rem_st, subs_set)
    #     # if tot != None:
    #     #    tot = list(tot)[0]
    #     #    i += len(tot)
    #     #    res +=  b
    #     # else:
    #     #     res += a
        #     i += 1 
    return res

 


print(buildString(apd_0,cop_0,s_0))