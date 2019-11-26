
apd_0= 4 
cop_0 = 5
s_0 = "aabaacaba"

apd_1= 8 
cop_1= 9
s_1= "bacbacacb"

apd_2= 7890 
cop_2= 7891 
s_2= "acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh"

def get_substrings(s,a,b):
    n = len(s)
    subs = set()
    for i in range(n): 
        for x in range(i+1,n+1): 
                subs.add(s[i:x])
    return subs

def find_substring(s, sub):
    s_list= []
    s_list.append(s)
    tail = set(s_list)
    if len(tail &sub) > 0 :
        return tail & sub
    else:
        return find_substring(s[:-1],sub)


def buildString(a, b, s):
    res = 0
    substrings = get_substrings(s,a,b)
    res = find_substring(s[1:],substrings)
    return res

 


print(buildString(apd_0,cop_0,s_0))