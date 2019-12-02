testCases = {
    0: {
        "A" : 4,
        "B" : 5,
        "S" : "aabaacaba",
        "R" : 26
    },
    1:{
        "A" : 8, 
        "B" : 9,
        "S" :"bacbacacb",
        "R" : 42
    },
    2:{
        "A":2,
        "B":3,
        "S":'caaahqcqes',
        "R" :20
    },
    3:{
        "A" : 1, 
        "B" : 3,
        "S" : 'acbbqbbqbb',
        "R" :10
    },
    4:{
        "A" : 2, 
        "B" : 4,
        "S" : 'cbabecbahe',
        "R" : 18
    },
    5:{
        "A" : 2, 
        "B" : 4,
        "S" : 'baaceacmbaaceam',
        "R" : 22
    },
    6:{
        "A" : 1, 
        "B" : 1,
        "S" : 'acabsbccbgfeaca',
        "R" : 13
    },
    7:{
        "A" : 2, 
        "B" : 4,
        "S" : 'acabccadeljadel',
        "R" : 26
    },
    8:{
        "A" : 1, 
        "B" : 2,
        "S" : 'cbaasgcbiikaegcbiidcbaasgcbiikaegcbiidir',
        "R":20
    },
    9:{
        "A" : 1, 
        "B" : 3,
        "S" : 'cabcjpsdaedsasedsascabcjpsddsdaedsasedsa',
        "R":24
    },
    10:{
        "A" : 2, 
        "B" : 3,
        "S" : 'cbacojcrojcrlidickjcjcrojcrlijcrojcrrojq',
        "R":45
    },
    11:{     
        "A" : 1, 
        "B" : 3,
        "S" : 'caacctinbnatinbnaqaacctinbnatinbnainbnatigaeifcaac',
        "R" : 29
    },
    12:{
        "R" : 50,
        "A" : 2,
        "B" : 4,
        "S" : 'bbaakbbabaptakbbabaptafbbabbaakbbabapcqkmbbabaptak'
    },
    13:{
        "R" : 50,
        "A" : 2, 
        "B" : 2,
        "S" : 'cbbcnkbbcbnkbbcbtnkatnbebgcbnkbgbcnkbbcbnkmbndnknk'
    },
    14:{
        "R":65040,      
        "A" : 2709,
        "B" : 2712,
        "S" : 'caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggihikncaomhikncaom'
    },
    15:{
        "R":126246,
        "A" : 7890,
        "B" : 7891,
        "S" : 'acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh'
    },
    16: {
        "R":268964,
        "A" : 7078,
        "B" : 7078,
        "S" : 'abbciabbcabciabbcmabbciabbcahlbchgcmabbcmggcmababciabbcagerafrciabbcsrhgcmcabciabbchgcmabbcmsfabcmsr'
    }

}



def build_a_string(a,b,s):
    cost = a
    i = 1
    match = ""
    while i < len(s):
        sub_st = s[:i]
        for j in range(i+1,len(s)+1):
            if s[i:j] not in s[:i]:
                if j == len(s)+1:
                    match = s[i:j]
                else:
                    match = s[i:j-1]
                break
            match = s[i:j]
        if a*len(match) > b:
            cost += b
            i += len(match)
        else:
            cost += a
            i += 1
    return cost


def build_a_string2(a,b,s):
    cost = [0]*len(s)
    cost[0] = a
    sub = ""
    i = 1
    while i < len(s):
        sub += s[i]
        while sub:
            if sub in s[:i+1-len(sub)]:
                break
            sub = sub[1:]
        if sub:
            cost[i] = min (cost[i-1]+a, cost[i-len(sub)]+b)
        else:
            cost[i] = cost[i-1]+a
        i += 1        
    return cost[-1]



n = 15
testcases = testCases[n]
print(build_a_string(testcases['A'], testcases['B'], testcases['S']), testcases['R'])

# print(build_a_string2(testcases['A'], testcases['B'], testcases['S']), testcases['R'])


