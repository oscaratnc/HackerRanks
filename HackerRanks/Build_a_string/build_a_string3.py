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

'''
Funciona para todos los casos, mientas el substring sub exista, es decir que contiene algun substring
encontrado, si al agarrar un elemento este no se encuentra en el substring dependiente de i sale del 
while y elimina ese elemento no repetido, dejando el string "vacio" , si  el string contiene elementos
toma el valor minimo de costo, de sumarle a al anterior o b a un costo anterior dependiente de la longitud
del substring encontrado y lo almacena en un arreglo de costos.
'''

def buildString(a,b,s):
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
print(buildString(testcases['A'], testcases['B'], testcases['S']), testcases['R'])



