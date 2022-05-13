"""
Georgia Institute of Technology - CS1301
HW03 - Strings and Lists
Name: Jihong Park
Collaboration Statement: None
"""

#########################################

"""
Function Name: movieNight()  
Parameters: subtitle (str)
Returns: fixed subtitle (str)
"""
def movieNight(subtitle):
    if len(subtitle) <= 0:
        return
    result = ""
    for x in subtitle:
        if not x.isdigit():
            result += x
    return result
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: longestWord()
Parameters: sentence (str)
Returns: longest word (str)
"""

def longestWord(sentence):
    if len(sentence) <= 0:
        return

    w = ""
    result = []
    sentence = sentence.replace(",","")
    for x in sentence:
        if x == " ":
            result.append(w)
            w = ""
        else:
            w += x
        
            
    result.sort(key = lambda x : len(x))
    word = result[len(result)-1]
    return word
# sentence = " Left foot, right foot, levitatin’ "
# print(longestWord(sentence))
# sentence = " Pop stars, Dua Lipa wit DaBaby "
# print(longestWord(sentence))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: tennisMatch()
Parameters: player1 (str), player2 (str), matchRecord (str)
Returns: game statement (str)
"""

def tennisMatch(player1, player2, matchRecord):
    p1_win = 0
    p2_win = 0
    result = matchRecord.split("-")
    for set in result:
        p1 = set.count("1")
        p2 = set.count("2")
        if p1 > p2: 
            p1_win += 1
        elif p2 > p1:
            p2_win += 1
        else:
            p1_win += 0
            p2_win += 0
    if p1_win > p2_win:
        return "{0} won! The score was {1}-{2}.".format(player1,p1_win,p2_win)
    elif p2_win > p1_win:
        return "{0} won! The score was {1}-{2}.".format(player2,p2_win,p1_win)
    else:
        return "It's a tie!"
# print(tennisMatch("Elizabeth","Michael","11221-222-1111-11121-22111-"))
# print(tennisMatch("Emily", "Kathleen", "1122-22211-11122-1212-"))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: freshFruit()
Parameters: barcodes (list), startIndex (int), stopIndex (int)
Returns: freshest barcode (int)
"""

def freshFruit(barcodes,startIndex,stopIndex):
    if len(barcodes) <= 0:
        return
    for i in range(startIndex,stopIndex+1):
        for j in range(i,startIndex,-1):
            if barcodes[j] < barcodes[j-1]:
                barcodes[j],barcodes[j-1] = barcodes[j-1],barcodes[j]
            else:
                break
    return barcodes[stopIndex]
#print(freshFruit([1312,2655,7823,4523,3212,8234],1,4))
#print(freshFruit([313414, 2241221, 32432, 49204, 493204,23212], 2, 4))



#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: highestSum()
Parameters: stringList (list)
Returns: highest sum index (int)
"""

def highestSum(stringList):
    result = []
    # cnt = 0
    # for x in stringList:
    #     for s in x:
    #         if s.isdigit():
    #             cnt += 1

    # if cnt == 0:
    #     x = 0
    for x in stringList:
        t = any(map(str.isdigit,x))
        if not t:
            x = 0

    for x in stringList:
        sum = 0
        for s in x:
            if s.isdigit():
                sum += int(s)
        result.append(sum)

    return result.index(max(result))
#print(highestSum(["fe72f8w","9df37!r2","8fe%w3wt8"]))
# print(highestSum(["90fe1wr3", "12432", "nfnqhu3","*@T$@21"]))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################




