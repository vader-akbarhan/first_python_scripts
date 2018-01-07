#Python exercise -- "Write a Python class to convert
#an integer to a roman numeral." (you should use a class):
#https://www.w3resource.com/python-exercises/class-exercises/

#Let's first show the Roman numerals:
#https://en.wikipedia.org/wiki/Roman_numerals
#Symbol     I   V   X   L   C   D   M
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

