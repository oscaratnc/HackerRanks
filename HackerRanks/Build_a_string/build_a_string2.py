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
   Divide el string en dos partes, sub parte izquierda
   y un remanente, se va tomando como substring de izqierda a derecha, y se revisa 
   el lado derecho hasta encontrar un string que se pueda formar del lado izquierdo 
   (substrings disponibles),  y se almacenan en match con condiciones para el momento de 
   no encontrar dicho substring y cortar el ciclo, se hace la cuantificacion de si el valor de 
   a * len(match) es mayor que b, copias y mueves el apuntador i dependiendo de la longitud de match.
   
   Este jala para algunos casos pero me arroja una diferencia 
   de 1 en algunos, apenas revisaré como puedo corregir eso o en 
   que es lo que falla. 
   '''
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

