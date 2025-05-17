# -*- coding: utf-8 -*-
"""
Created on Fri May 16 17:35:32 2025

@author: mmanz
"""

def isOperator(op):
    return (op == '+' or op == '*')

expression = "6+2*0+-4"

def traversal(exp):
    num = []
    opr = []
    tmp = ""

    # store operator and numbers in different vectors
    for i in range(len(exp)):
        if (isOperator(exp[i])):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]
    num.append(int(tmp))
    
    # when finding multiplication split num
    for i in range(len(opr)):
        if opr[i] == '*':
            break
    left = num[:i+1]
    right = num[i+1:]
    
    
    # getting max and min value of the left side of multiplication
    
    leftmaxvalue = 0  
    leftminvalue = 10**3
    
    for j in range(i):
        if opr[j] == '+' :
            value = []
    
            for k in range(len(left)):  
                temp = left[k]
                if leftmaxvalue < temp:
                    leftmaxvalue = temp
                if leftminvalue > temp:
                    leftminvalue = temp
                
                value.append(temp)
                for k in range(len(left)):
                 if leftmaxvalue < sum(value):
                    leftmaxvalue = sum(value)
                 if leftminvalue > sum(value):
                    leftminvalue = sum(value)

    # getting max and min value of the right side of multiplication
    
    rightmaxvalue = 0  
    rightminvalue = 10**3
    
    for j in range(i):
        if opr[j] == '+' :
            value = []
    
            for k in range(len(right)):  
                temp = right[k]
                if rightmaxvalue < temp:
                    rightmaxvalue = temp
                if rightminvalue > temp:
                    rightminvalue = temp
                
                value.append(temp)
                for k in range(len(right)):
                 if rightmaxvalue < sum(value):
                    rightmaxvalue = sum(value)
                 if rightminvalue > sum(value):
                    rightminvalue = sum(value)
    
    
    # test which parenthese will give the max value
    leftvalues = [leftmaxvalue,leftminvalue]
    rightvalues = [rightmaxvalue,rightminvalue]
    maxvalue = 0
    minvalue = 10**3
    for i in range(len(leftvalues)):
        for j in range(len(rightvalues)):
            temp = 0
            if leftvalues[i] == leftvalues[1] :
                temp += left[0]
            if  rightvalues[j] == rightvalues[0]:
                temp += right[-1]
             
            temp += rightvalues[j] + leftvalues[i] 
            
        if temp > maxvalue:
            maxvalue = temp
            
    return(maxvalue)

