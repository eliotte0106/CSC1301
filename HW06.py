"""
Georgia Institute of Technology - CS1301
HW06 - Text Files
Name: Jihong Park
Collaboration Statement:
"""

#########################################

"""
Function Name: findCuisine()  
Parameters: filename (str), cuisine (str)  
Returns: list of restaurants (list)
"""
def findCuisine(file,cuisine):
    f = open(file,"r")
    lst = f.read()
    f.close()
    lst = lst.strip().split("\n")

    result = []

    for i in range(len(lst)):
        if lst[i] == cuisine:
            result.append(lst[i-1])
            
    return result


# print(findCuisine("restaurants.txt","NotACuisine"))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: restaurantFilter()  
Parameters: filename (str)
Returns: dictionary that maps cuisine type (str)
to a list of restaurants of the same cuisine type (list)
"""

def restaurantFilter(filename):
    f = open(filename,"r")
    lst = f.read()
    f.close()
    lst = lst.strip().split("\n")

    result = dict()

    for i in range(1,len(lst),4):
        result[lst[i]] = []
    for i in range(1,len(lst),4):
        result[lst[i]].append(lst[i-1])

    return result

#print(restaurantFilter("restaurants.txt"))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: createDictionary()  
Parameters:  filename (str), output filename (str)
Returns: None (NoneType)
"""

def createDirectory(filename,directory):
    f = open(filename,"r")
    lst = f.read()
    lst = lst.strip().split("\n")
    f.close()

    ff_result = []
    sd_result = []

    for i in range(2,len(lst),4):
        if lst[i] == "Fast Food":
            ff_result.append(lst[i-2]+" - "+lst[i-1])
        else:
            sd_result.append(lst[i-2]+" - "+lst[i-1])

    ff_result.sort()
    sd_result.sort()

    f2 = open(directory,"w")
    f2.write("Restaurant Directory\n")
    f2.write("Fast Food\n")

    for i in range(len(ff_result)):
        f2.write(str(i+1)+". "+ff_result[i]+"\n")

    f2.write("Sit-down\n")

    for i in range(len(sd_result)-1):
        f2.write(str(i+1)+". "+sd_result[i]+"\n")

    f2.write(str(len(sd_result))+". "+sd_result[len(sd_result)-1])
    f2.close()

#createDirectory("restaurants-1.txt","directory.txt")

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: countNominations()  
Parameters:  filename (str), category (str)
Returns: tuple that holds winning movie name (str) and number of nominations (int)
"""

def countNominations(filename,category):
    f = open(filename,"r")
    lst = f.readlines()
    award = []

    for x in lst:
        s = x.strip().split("\n")
        s = "".join(s)
        award.append(s)

    f.close()

    result = tuple()
    cnt = 0
    winner = ""

    if len(category) <= 0:
        return result

    for i in range(len(award)):
        if award[i] == category and award[i+2] == "Winner":
            winner = award[i+1]
            
    for x in award:
        if winner in x:
            cnt += 1

    result = (winner,cnt)

    return result

# cat = 'Best Animated Feature Film'
# cat2 = 'Best Visual Effects'
#print(countNominations("academyawards.txt",""))



#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: categories()  
Parameters:  filename (str), category list (list)
Returns: dictionary that maps categories (str) to lists (list) holding tuples with the corresponding nominations (str)
"""

def categories(filename,category):
    if len(category) < 0:
        return

    f = open(filename,"r")
    lst = f.readlines()
    award = []

    for x in lst:
        s = x.strip().split("\n")
        s = "".join(s)
        award.append(s)

    f.close()
    result = dict()
    
    for x in category:
        result[x] = []

    for x in category:
        for i in range(len(award)):
            if award[i] == x:
                award[i+1]=award[i+1].replace(" (", ",")
                award[i+1]=award[i+1].replace(")","")
                award[i+1] = award[i+1].split(",")
                result[x].append(tuple((award[i+1])))
            # elif award[i] == x:
            #     result[x].append(tuple((award[i+1])))

    return result
# categorylist = ['Best Original Score','Best Actress']
#print(categories('academyawards.txt',['Best Original Score','Best Actress']))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: winnerFormat()  
Parameters:  readfile (str), output filename (str), category (str)
Returns: None (NoneType)
"""

def winnerFormat(readfile,writefile,category):
    if len(category) <= 0:
        return

    f = open(readfile,"r")
    lst = f.readlines()
    award = []

    for x in lst:
        s = x.strip().split("\n")
        s = "".join(s)
        award.append(s)

    f.close()

    result = []
    winner = ""

    for i in range(len(award)):
        if award[i] == category and award[i+2] == "Winner":
            winner = award[i+1]
            result.append(winner)
    for i in range(len(award)):
        if award[i] == category and award[i+2] == "Nominated":
            result.append(award[i+1])

    f2 = open(writefile,"w")
    f2.write(category+"\n")
    f2.write("\t1. *Winner* "+result[0]+"\n")
    for i in range(1,len(result)-1):
        f2.write("\t"+str((i+1))+". "+result[i]+"\n")
    f2.write("\t"+str(len(result))+". "+result[len(result)-1])
    f2.close()

# winnerFormat("academyawards.txt","category.txt","Best Sound")



#########################################
########## WRITE FUNCTION HERE ##########
#########################################



