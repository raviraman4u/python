#!/usr/bin/env python
# coding: utf-8

# # Basic Concepts and programing

# ### Python Basic Programming

# In[15]:


a#Write a Program ( WAP ) to print hello world

print('Hello World Ravi!')
print("Hello World Raman!")


# In[16]:


# Declare the following variables:
#Int, Float, Boolean, String & print its value.

# Integer variable 

integer_variable = 5

print(integer_variable)
print(type(integer_variable))

# Float variable 
float_variable = 10.2
print(float_variable)
print(type(float_variable))

# String variable 
string_variable_1 ='Ravi'
print(string_variable_1)
print(type(string_variable_1))

string_variable_2 ="Raman"
print(string_variable_2)
print(type(string_variable_2))

# Boolean variable 

boolean_variable_1 = True
print(boolean_variable_1)
print(type(boolean_variable_1))

boolean_variable_2 = False
print(boolean_variable_2)
print(type(boolean_variable_2))


# In[24]:


#Program to calculate the Area of Triangle based on given height and base

triangle_base = input("Enter triangle base : ")
triangle_height = input("Enter triangle height : ")
triangle_area = 1/2 *(int(triangle_base)* int(triangle_height))

print("The area of triangle is : ", triangle_area )


# In[11]:


#Program to swap two variables using temp variable

fisrt_variable = 10
second_variable = 20
temp_variable = None

print("Before swapping value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))

temp_variable = fisrt_variable
fisrt_variable = second_variable
second_variable = temp_variable

print("After swapping value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))

# Program to swap two String variables without using temp variable, using constructer
fisrt_variable = "Ravi"
second_variable = "Raman"

print("Before swapping with default constructer value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))
fisrt_variable,second_variable = second_variable,fisrt_variable
print("After swapping with default constructer value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))

# Program to swap two integer variables without using temp variable

fisrt_variable = 5
second_variable = 3

print("Before swapping with integer value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))

fisrt_variable = fisrt_variable + second_variable

second_variable = fisrt_variable - second_variable

fisrt_variable = fisrt_variable - second_variable

print("After swapping with integer value of first_variable is : {} and value of second variable is : {}".format(fisrt_variable,second_variable))


# In[18]:


#Program is to check if a number is positive, negative or 0 
# Input a valid number else exception will be thrown. Will handle exceptions later part of the code
input_number = int(input(" Enter a valid number : "))

if(input_number > 0):
    print("The number entered {} is positive".format(input_number))
elif(input_number == 0):
    print("The number entered {} is zero".format(input_number))
elif(input_number < 0):
    print("The number entered {} is negative".format(input_number))
else:
    print("oo lala god knows what's in your mind")

    


# In[22]:


#Program is to check if a number is even or odd
input_number = int(input(" Enter a valid number : "))

if (input_number < 0):
    print("The number entered {} is invalid ".format(input_number))
elif(input_number == 0):
    print("The number entered {} is even".format(input_number))
elif(input_number % 2 ==0):
    print("The number entered {} is even".format(input_number))
else:
    print("The number entered {} is odd".format(input_number))
    


# In[29]:


#Program to print Odd number within a given range
range_start = int(input(" Enter a range start number : "))
range_end = int(input(" Enter a range end number : "))

for each_number in range(range_start,range_end):
    if (each_number % 2 != 0):
        print("The number {} is odd".format(each_number))
    else:
        continue


# In[49]:


#Program to find the factorial of a number

factorial_input_number = int(input(" Enter a valid number to get the factorial value : "))

factorial_output = None

for each_number in range(factorial_input_number,0,-1):
    if (factorial_input_number == each_number):
        factorial_output = each_number
    else:
        factorial_output = factorial_output * each_number
    
print("Factorial value for number {} is {}".format(factorial_input_number,factorial_output))
    


# In[61]:


# Program to reverse a given number

# Note if a number ending with zero then convert the number to String data type and use format to display leading zeros.

reversal_input_number = int(input(" Enter a valid integer number to reverse : "))
print("Input number is : {}".format(reversal_input_number))
reversal_output_number = 0
# If we do modulus operation by 10 then either we will get the last digit as zero or non zero number
while(reversal_input_number > 0):
    last_digit_number = reversal_input_number % 10
    
    # We need to cpature the reversed number ( last digit)

    reversal_output_number = (reversal_output_number *10) + last_digit_number
    print(reversal_output_number)
    # Now the from input number we need to remove the last digit as it's already got captured above

    reversal_input_number = int(reversal_input_number / 10)
   
print("After reversal number is : {}".format(reversal_output_number))


# In[69]:


#Program to find out the sum of Natural numbers

natural_number_range_start = int(input(" Enter natural number range start value : "))
natural_number_range_end = int(input(" Enter natural number range end value : "))
sum_natural_numbers =0

if(natural_number_range_start > 0 and natural_number_range_end > 0 ):
    
    if(natural_number_range_end < natural_number_range_start):
        
        print("Natural number start range must be lesser than end range value.")
    else:
        
        for each_natural_number in range(natural_number_range_start,natural_number_range_end + 1, 1):
            sum_natural_numbers +=each_natural_number
            
        print("Sum of natural number for range {} till this {} is {}".format(natural_number_range_start,natural_number_range_end,sum_natural_numbers))    
    
            
else:
    print("Input values should must be greater than 0")
    




# ### Python Strings

# In[86]:


#Program to reverse a string without using recursion

input_string = input(" Enter your string which needs to be reversed : ")

reversed_string =""
# Check if string is empty or not then only proceed
if(input_string and input_string.strip()):
         
    for each_character in input_string:
        reversed_string = each_character + reversed_string
    print(" Input String is : {} and it's reversed is : {}".format(input_string,reversed_string))
        
else:
    print("Invalid String !!!")

# Another way of doing is with slice
if(input_string and input_string.strip()):
    print("Reversed String using slice is : ", input_string[::-1])
else:
    print("Invalid String !!!")
    


# In[107]:


# Program to check if string is palindrome or not
input_string = input(" Enter your string which needs to be checked for palindrom : ")

# Using Loops
if(input_string and input_string.strip()):
    for each_character_index_position in range(0, int(len(input_string)/2)):
        if input_string[each_character_index_position] != input_string[len(input_string)-each_character_index_position-1]:
            print("The given string {} is not palindrome".format(input_string))
        else:
            print("The given string {} is palindrome".format(input_string))

else:
    print("Invalid String !!!")
    
# Another way using slicing to achive the same

# Check if string is empty or not then only proceed
if(input_string and input_string.strip()):
 
    if(input_string == input_string[::-1]):
        
        print("The given string {} is palindrome".format(input_string))
    else:
        print("The given string {} is not palindrome".format(input_string))
else:
    print("Invalid String !!!")
 


# In[112]:


# Python Program to Replace all Occurrences of ‘a’ with $ in a String

input_string = input(" Enter your string : ")
if(input_string and input_string.strip()):
    
    final_replaced_string = input_string.replace('a','$')
    print("Input String is : {} and after replacing all 'a' with '$' is {}".format(input_string,final_replaced_string))
    
else:
    print("Invalid String !!!")    


# In[120]:


# Python Program to Count the Number of Vowels in a String

string_vowels ="aeiou"
input_string = input(" Enter your string : ")
vowels_count=0
if(input_string and input_string.strip()):
    lowercase_input_string = input_string.lower()
    for each_vowel in string_vowels:
        if(lowercase_input_string.find(each_vowel)!=-1):
            vowels_count+= lowercase_input_string.count(each_vowel,0,len(input_string))
        else:
            continue
    print("The total numbers of vowels in the string {} is : {}".format(input_string,vowels_count))

else:
    print("Invalid String !!!")      


# In[8]:


# Python Program to Input Two Strings and Display the Larger String without Using Built-in Functions

input_string1 = input("Enter first string: ")
input_string2 = input("Enter second string: ")
string1_count = 0
string2_count = 0

for each_character_in_string1 in input_string1:
    string1_count = string1_count + 1

for each_character_in_string2 in input_string2:
    string2_count = string2_count + 1

if (string1_count < string2_count):
    print ("Larger string is : {}".format(input_string2))

    
elif (string1_count == string2_count):
    print ("Both strings {} and {} are equal.".format(input_string1,input_string2))
else:
    print ("Larger string is : {}".format(input_string1))


# In[13]:


# Count the number of digits & letter in a string

input_alpanumeric_string = input("Enter alpha numeric string: ")

digit_counter =0
letter_counter =0
somethingelse_counter = 0
for input_alpanumeric_character in input_alpanumeric_string:
    if(input_alpanumeric_character.isdigit()):
        digit_counter+=1
    elif (input_alpanumeric_character.isalpha()):
        letter_counter+=1
    else :
        somethingelse_counter+=1

print("For input string : {} number of digits are : {}, no of letters are : {} and non alphanumeric values are : {}".format(input_alpanumeric_string,digit_counter,letter_counter,somethingelse_counter))
    
    


# In[16]:


#Count Number of Lowercase Characters in a String

input_string = input("Enter your string: ")

lowercase_string_counter =0
for input_string_character in input_string:
    if(input_string_character.isalpha() and input_string_character.islower()):
        lowercase_string_counter+=1
    elif (input_string_character.isdigit()):
        continue
    else :
        continue

print("For input string : {} number of lowercase characters are : {}".format(input_string,lowercase_string_counter))
 


# In[30]:


# Program to check if a Substring is Present in a Given String

input_string = input("Enter your main string: ")
input_sub_string = input("Enter your sub string: ")

if(input_string.find(input_sub_string)!= -1):
    print("Input sub string : {} found in provided main string : {}".format(input_sub_string,input_string))
else:
    print("Input sub string : {} doesn't exists in provided main string : {}".format(input_sub_string,input_string))


# ### List and Tuples

# In[31]:


# Program to Find the Largest Number in a List


input_number_list = [int(each_input_number) for each_input_number in input("Enter the list items seperated by space : ").split()]  
      



if(len(input_number_list) == 0):
    print("The list is empty")
else:
    # Let's assume the fisrt number is max number in the list 
    max_number = input_number_list[0]
    # using for loop
    for each_number in input_number_list:
        if(each_number > max_number):
            max_number = each_number

    print(" Max number using forloop is ", max_number)

    #  Another appraoch by using sorting the list in ascending order

    input_number_list.sort()

    print(" Max number in the list using reverse index is : ",input_number_list[-1])

    print(" Max number in the list using max funtion is : ",max(input_number_list))


            
        


# 

# In[34]:


# Program to Put Even and Odd elements in a List into Two Different Lists

input_odd_even_number_list = [int(each_input_number) for each_input_number in input("Enter the list items seperated by space : ").split()]

even_number_list = []
odd_number_list = []
if(len(input_number_list) == 0):
    print("The list is empty")
else:
    for each_number in input_odd_even_number_list:
        if(each_number == 0):
            even_number_list.append(each_number)
        elif(each_number % 2 == 0):
            even_number_list.append(each_number)
        else:
            odd_number_list.append(each_number)
    print("For given input list : {} the even list is : {} and odd list is : {}".format(input_odd_even_number_list,even_number_list,odd_number_list))

 


# In[13]:


# Program to Read a List of Words and Return the Length of the Longest One:
input_words_list = [each_input_word for each_input_word in input("Enter the list words seperated by space : ").split()]

if(len(input_words_list) == 0):
    print("No Word entered")
else:
    # Let's assume the fisrt word is having max length and longest word
    
    max_word_length = len(input_words_list[0])
    max_length_word = input_words_list[0]
    # using for loop
    for each_word in input_words_list:
        if(len(each_word) > max_word_length):
            print("max_length_word",max_length_word)
            max_word_length = len(each_word)
            max_length_word = each_word

    print(" For given input word list : {} the longest word is : {} having length : {}".format(input_words_list,max_length_word,max_word_length))
    


# In[24]:


# Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
input_number_tuple = tuple(int(each_input_number) for each_input_number in input("Enter the list items seperated by space : ").split())

if( len(input_number_tuple) == 0):
    print("No Numberes entered for the tuple")
else:
    #input_number_tuple = tuple(input_number_list)
    list_of_tuples = []
    
    for each_number_in_tuple in input_number_tuple:
        square_root_number = each_number_in_tuple*each_number_in_tuple
        list_of_tuples.append(tuple([each_number_in_tuple,square_root_number]))
    print(" For entered tuple : {} the list of tuples will be : {}".format(input_number_list,list_of_tuples) )

        
        
        


# In[29]:


# Program to Remove the Duplicate Items from a List

input_number_list = [int(each_input_number) for each_input_number in input("Enter the list items seperated by space : ").split()]

if(len(input_number_list) == 0):
    print("The list is empty")
else:
    distinct_list = []
    [distinct_list.append(each_number) for each_number in input_number_list if each_number not in distinct_list]
    print("Entered list of numbers : {} and distinct list of numbers {}".format(input_number_list,distinct_list) ) 


# In[ ]:




