'''
You are given a string S. Count the number of occurrences of all the digits in the string S.

Input:
First line contains string S.

Output:
For each digit starting from 0 to 9, print the count of their occurrences in the string S. So, print
lines, each line containing 2 space separated integers. First integer i and second integer count of occurrence of i. See sample output for clarification. 

sample input =77150
sample output = 
                    0 1
                    1 1
                    2 0
                    3 0
                    4 0
                    5 1
                    6 0
                    7 2
                    8 0
                    9 0
@author: Aasif Multani
'''

if __name__ == '__main__':
    user_input = input()
    zero = one = two = three = four = five = six = seven = eight = nine = 0
    for temp in range(len(user_input)):
        digit_value = user_input[temp]
        if digit_value == '0':
            zero = zero + 1;
        if digit_value == '1':
            one = one + 1;
        if digit_value == '2':
            two = two + 1;
        if digit_value == '3':
            three = three + 1;
        if digit_value == '4':
            four = four + 1;
        if digit_value == '5':
            five = five + 1;
        if digit_value == '6':
            six = six + 1;
        if digit_value == '7':
            seven = seven + 1;
        if digit_value == '8':
            eight = eight + 1;
        if digit_value == '9':
            nine = nine + 1;
    
    
    print('0',zero)
    print('1',one)
    print('2',two)
    print('3',three)
    print('4',four)
    print('5',five)
    print('6',six)
    print('7',seven)
    print('8',eight)
    print('9',nine) 
    print('10',ten)        
            
        
        
        
    