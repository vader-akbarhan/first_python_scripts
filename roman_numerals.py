#Python exercise -- "Write a Python class to convert
#an integer to a roman numeral." (you should use a class):
#https://www.w3resource.com/python-exercises/class-exercises/

#Let's first show the Roman numerals:
#https://en.wikipedia.org/wiki/Roman_numerals
#Symbol I   V   X   L   C   D   M
#Value  1   5   10  50  100 500 1000

class All_Roads_Lead_To_Rome:   
    def Extract_decimally(self): #WORKS!
        global number_input
#        number_input = str(input("Enter an Indian number: "))
        number_input = str("12345")
        #global the_list
        if len(number_input)>4:
            print("Romans di no not have a notation for numbers higher than 9999.")
        else:
            the_list = []
            for i in number_input[::]:
                the_list.append(i)
            return(the_list)
    def New():
        instance2 = All_Roads_Lead_To_Rome()
        decimal_list2 = instance2.Extract_decimally()
        print(decimal_list2)
    def Tell_me(self): 
        print(("The number is a sum of {} thousand(s), {} hundred(s), {} ten(s), and {} one(s). ")
        .format(*the_list)) #WORKS! And I used *args! # And I wrapped lines of code. 

if __name__ == '__main__':
    instance = All_Roads_Lead_To_Rome()
    decimal_list = instance.Extract_decimally() #WORKS! 
    tell = instance.Tell_me()

#Work in progress. 
#Error: 
# Traceback (most recent call last):
#  File "/media/user1/New Volume/IT studies/Python/roman_numerals.py", line 34, in <module>
#    tell = instance.Tell_me()
#  File "/media/user1/New Volume/IT studies/Python/roman_numerals.py", line 29, in Tell_me
#    .format(*the_list)) #WORKS! And I used *args! # And I wrapped lines of code.
#NameError: global name 'the_list' is not defined
#
#I am trying to track the namespaces so that I find what is wrong. Additionally: 
# def Tell_me(self): 
#        nonlocal the_list
#        print(("The number is a sum of {} thousand(s), {} hundred(s), {} ten(s), and {} one(s). ")
#        .format(*the_list)) #WORKS! And I used *args! # And I wrapped lines of code. 
#
# ... gives "SyntaxError: invalid syntax". I am still looking into the namespaces. 

# After I fix the above issue, I will write a function (of the same class) which will substitute, 
# say, 100 with "C" and "50" with "L". I intend to determine whether there is, say, 50 to be written, 
# by dividing the corresponding number from "the_list" using modulo. For example: 90 % 50 = 40 -->
# --> yes, write a "L" (50); then work with the remainder (40). 


