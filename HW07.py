"""
Georgia Institute of Technology - CS1301
HW07 - CSV Files
Name: Jihong Park
Collaboration Statement:
"""

#########################################

"""
Function Name: extraHours()  
Parameters: filename (str), hour (int)  
Returns: list of (person, extra money) tuples (tuple)
"""
from os import X_OK


def extraHours(filename, hour):
    f = open(filename,"r")
    f.readline()
    lst = f.readlines()
    f.close()
    result = []
    for x in lst:
        x = x.strip().split(",")
        money = 0
        if int(x[4]) <= hour:
            continue
        else:
            money = int(x[2]) * (int(x[4])-hour)
            result.append((x[0],money))
    return result
#print(extraHours("employees.csv",35))

        
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: seniorStaffAverage()  
Parameters: filename (str), year (int)
Returns: average age of senior staff members (float)
"""
def seniorStaffAverage(filename, year):
    f = open(filename,"r")
    f.readline()
    lst = f.readlines()
    f.close()
    age = 0
    cnt = 0
    for x in lst:
        x = x.strip().split(",")
        if int(x[3]) >= year:
            continue
        else:
            age += int(x[1])
            cnt += 1
    if cnt == 0:
        return 0.0
    else:
        return round(age/cnt,2)
#print(seniorStaffAverage("employees.csv",2017))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: ageDict()  
Parameters:  filename (str), list of age ranges (list)
Returns: dictionary of age ranges (dict)
"""
def ageDict(filename, range_lst):
    f = open(filename,"r")
    f.readline()
    lst = f.readlines()
    f.close()
    dic = dict()
    for x in range_lst:
        dic[x] = []
    for x in lst:
        x = x.strip().split(",")
        for y in range_lst:
            z = y.split("-")
            if int(x[1]) >= int(z[0]) and int(x[1]) <= int(z[1]):
                dic[y].append(x[0])
    for k, v in dict(dic).items():
        if len(v) == 0:
            del dic[k]
    
    #other way
    # for x in list(dic):
    #     if len(dic[x]) == 0:
    #         del dic[x]
    return dic
# rangelist = ["0-18","18-19"]
# print(ageDict("employees.csv",rangelist))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""Function Name: perfectDay()
Parameters: filename (str), temperature range (tuple)
Returns: list of dates (list)
"""
def perfectDay(filename, temp_range):
    f = open(filename,"r")
    f.readline()
    lst = f.readlines()
    f.close()
    result = list()
    for x in lst:
        x = x.strip().split(",")
        if temp_range[0] >= int(x[1]) and temp_range[0] <= int(x[2]) and temp_range[1] >= int(x[1]) and temp_range[1] <= int(x[2]):
            result.append(x[0])
    return result
#print(perfectDay("weather.csv",(55, 60)))
#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: tempRange()
Parameters: filename (str), dates (list)
Returns: date and temperature range (tuple)
"""
def tempRange(filename, date_lst):
    f = open(filename,"r")
    f.readline()
    lst = f.readlines()
    f.close()
    result = []
    max = ("",0)
    for x in lst:
        x = x.strip().split(",")
        result.append((x[0],int(x[2])-int(x[1])))
    for x in result:
        for y in date_lst:
            if x[0] == y and int(x[1]) > max[1]:
                max = x
    return max

#print(tempRange("weather.csv",['6/3', '7/3', '10/3', '13/3']))

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


