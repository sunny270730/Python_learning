#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###     variable     ###

number = 100      # integer value #
rating = 4.5      # floating value #
string = 'sunny kumar'  # string value #


# number 100 :- this is a int value 
# 4.5 is a floating value 
# string is character of alphabet like 'sunny kumar' is called  variable 

# In[3]:


####### input function #######  

name = input('what is your name?:- ')      # input function #
favorite_singer = input('what is your favorite singer name?:- ') # input function# #
print(name + ' like  '+ favorite_singer + ' songs') # print the output #




# input function are used to enter the input in help of the variable
# 

# In[6]:


#### type conversion #####


birth_year = input('birth_year: ')    # input function #
print(type (birth_year))                 # type function # 
age = 2023 - int(birth_year)     # age is calculate the birth_year #
print(type (age))             # type of function #
print(age)            # print the output #



my_weight_lbs = input('weight (lbs): ')
weight_kg = int(my_weight_lbs) * 0.45
print(weight_kg)



# Type conversion is a  used the type function and declare the input type like:-
# int, float, string, boolean, etc

# In[17]:


#####  string ######

course = 'pyhton for start me '   # this statement is string statement #
print(course [0:10])            # this is used the printing the string statement #


course = 'pyhton for start me '   # this statement is string statement #
print(course [1:-2])            # this is used the printing the string statement #


course = 'pyhton for start me '   # this statement is string statement #
print(course [:])            # this is used the printing the string statement #


name = 'sunny kumar'
print(name[1:-1])


#  string statement  are using the python program in any statement are used single quoate is called string

# In[23]:


###   formatted string #####

first = 'sunny'
last = 'kumar'
msg = first + '[' + last +'] is a coder'    # msg are stored the string data #
msgg= f'{last} [{first}] is a codder'
print(msgg)
print(msg)









# In[16]:


### string methods ###


course = 'pyhton for start me '   # this statement is string statement #
print(len (course) )            # this is using the len function and count the all string number   #
course.upper()
print(course.upper())           # this is use the upper case alphabet #
print(course.lower())           # this is use the lower case alphabet #



course = 'python for start me'
print(course.find('start'))           # they are find the string number #



course = 'python for start codding'
print(course.replace('start','jupyter notebook and start')) # replace function are used replace the any qurry/value #


course = 'python for start codding'
print('Python' in course)                  #  there are check the condition for using in operater  #




 




# <!-- # there are using the string methods #
# 
# # course = 'my name is sunny kumar '
# # len(course)
# # course.upper()
# # course.lower()
# # course.find()
# # course.replace()
# # '....' in course
#  -->

# In[22]:


### Arithmetic Operations ###

 
x = 15                         # there are using arithmetic operation #
# x = (x+2),(x-2),(x * 3),(x/3),(x % 3) ,(x ** 10), (x // 2)
x += 3
print(x)






# In[27]:


###   Operator precedence ###
   
x = 15 + 3 * 5 ** 5   
print(x)    

   
y = (15-5)*4+2-2  
print(y)
   
   


# Operator precedence which means the order of operations. Multiple operator a higher precedence which means it's applied fitrst which means (3 * 5)=15
# the secound addition for 15 + 15 =30
# 
# There are order of expersion like 
# -> exponentiation 2**3
# -> multipilcation or division
# -> addition or subtraction
# 

# In[42]:


#### Math Functions ####
   
x = 3.6
print(round(x))
print(abs(-3.6))      # Then absolute always returns a positive number #


# In[33]:


import math
print(math.floor(3.6))   ## there are using the math function in using import math libaray



# In[49]:


#### if statements ###
is_cat = False
is_dog = False

if is_cat:                     
    print("yes")
    print('this is a cat')
elif is_dog:
    print('this is a dog')
    
else:
    print('dog are practice for running')
    print('this is a dog')


print('pet color black')    


# In[55]:


amount = 1500
my_amount = False

if  my_amount:
   month_salary = 30 * amount
   
   
else:
   month_salary = 20 * amount
print(f"Month salary :{month_salary}")


# In[62]:


#### Logical Operators ######


high_amount = True
high_credit = True

if high_amount and not high_credit:
    print('accepts this profile loan')


    
 


# There are used the logical operators like.
# AND
# OR
# NOT

# In[10]:


####   Comparison Operators  ####


# skill = 23

# if skill > 20:              # this is using the comparision operators #
#     print('this is a coder')
# else:
#     print('this is  not a coder ')

name = 's'

if len(name) < 3:
    print(' there are three character of string')
elif len(name) > 20:
    print('ther are 20 character if string ')
else:
    print('goood bye dear')
    
    



# there are comparision operators this is using the if conditions like operators:->
# 
# 
# >  --> greater then,
# 
# <  --> less then,
# 
# => --> equal to less then,
# 
# >= --> greater then equal to,
# 
# != --> not equal to,
# 
# == --> equal (assignment operator),

# In[19]:


#### weight converter program ####

weight = int(input('weight : '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"you are {convert} kilos")
else:
    convert = weight / 0.45
    print(f"you are {convert} pounds")





#  there are using the weight converting program help of if condition

# In[30]:


#### while loops  ####



i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('done')





# There are the while loop using the condition check and repeat the code is condition false then program excuate the loops then print the output is called while loops 
# 

# In[2]:


####  building a Guessing game #####

secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won!')
    
    





# In[7]:


######    building the car game #########

command = ""
started = False
while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print('car is already started !')
        else:
            started = True
            print('car start.')
    elif command == "stop":
        if not started:
            print('car is already stopped !')
        else:
            started = False
            print('car stopped.')
    elif command == "help":
        print(""" start-> start the car 
                stop-> car stopped
                quit->exit """)
    elif command == " quit":
        break
    else : 
        print(' there are not understand the')
    





# In[8]:


##### for loops #####

i = [1,2,4,5,3,6,8,9,7]
for i in range(0,8):
    print(i)






# In[29]:


command = " "
while command !="exit":
    employee_no = input("Employee No: ")
    if not employee_no:
        break
    employee_no = int(employee_no)
    
    employee_name = input("Employee Name: ")
    if not employee_name:
        break
    
    employee_salary = input("Employee Salary: ")
    if not employee_salary:
        break
    employee_salary = float(employee_salary)
    
    employee_address = input("Employee Address: ")
    if not employee_address:
        break
    
    employee_married_str = input("Employee Married? (y/n): ")
    if not employee_married_str:
        break  
    command=str(input("Enter exit to exit and anything else to continue"))
    employee_married = employee_married_str.lower() == 'y'
    
    
    print("Employee No:", employee_no)
    print("Employee Name:", employee_name)
    print("Employee Salary:", employee_salary)
    print("Employee Address:", employee_address)
    print("Employee Married?", employee_married)

    
        



# In[3]:


employee_married = input('employee married?:- True or False')
if employee_married == "True":
    print('employee married')
if employee_married == "False":
    print('employee not married')


# In[14]:


##### for  loops #####

price = [10,20,40]

total = 0
for pricess in price:
    total += pricess
print(f"Total: {total}")


# In[10]:


####      Nested loops #######
  
# num = [5, 2, 5, 2, 2]

# for i in num:
#     print(" *" * i)

   
num = [1, 2, 3, 4, 5, 4, 3, 2, 1]

for i in num:
   print("*" * i)
   
   


# In[9]:


###### assignment 2 #########




flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}
flow_1["api_data"]["url"] = "https://newurl.com/"      #### update url######
flow_2["api_data"]["url"] = "https://newurl.com/"
flow_3["api_data"]["url"] = "https://newurl.com/"


print(flow_1["api_data"]["url"], flow_2["api_data"]["url"],flow_3["api_data"]["url"]) ####    fetch url    ######
flow_3["entities"].append({"entity": "price_range", "prompt": "Please enter your desired price range ?"})   ### New entity ###

print(flow_3)
flow_1["entities"].remove({"entity": "product", "prompt": "can you please enter what are you searching ?"}) ###### delete entity###
print(flow_1)

      
      
      
      
      
      
      
      
      
      
      
      
      
# 1) Fetch all Urls from the dict
# 2) Add new entity in flow_3
# 3) Update url in all flow
# 4) Delete the entity in flow_1      


# In[11]:


#######       list    #########

# names = ['sunny', 'jimmy', 'mani', 'mohit']
# names[2] = 'manpreet'
# print(names)

numbers = [ 3,4,5,6,7,8,9,12]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)





# 
# 
# Good morning sir 
# First of all , thank you for giving me this oppurtunity to introduce myself 
# .My name is sunny kumar. i am basically from malout but currently staying in patiala. i did my graduation in Bca from MIMIT MALOUT. currently i am pursuing Mca in punjabi universtiy Patiala. my strength are i am motivated hard working and a disciplined person my short term goal is to get a job in a it companys and my long term goal is to achieve a good position  where i can build my career and help the organization too.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[3]:



####         2D list      ######

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for item in row:
        print(item)










# In[2]:


##### list method ####
number = [5,2,1,7,4]
number.append(0)
print(number)

number = [5,2,1,7,4]
number.insert(0,10 )
print(number)

number = [5,2,1,7,4]
number.remove(1)
print(number)

number = [5,2,1,7,4]
number.pop()
print(number)

number = [5,2,1,7,4]
number.clear()
print(number)
number = [5,2,1,7,4]
print(number.index(7))

number = [5,2,1,7,4]
number.sort()
number.reverse()
print(number)

number = [5,2,1,7,4]
number2 = number.copy()
print(number2)



# In[5]:


print("enter the number")
number = int(input())
temp = number
reverse = 0
while(number>0):
    dig = number%10
    reverse = reverse *10 + dig
    number = number//10
print(reverse)
if temp == reverse:
    print("Number is a palindrome ")
else:
    print("Number is not a palindrome")


# In[3]:


###### Tuple ########



coodinates = (1,2,3)
x,y,z, = coodinates
print(z)



# In[2]:


#######    Dictinaries ###########

customer = {"name":"sunny kumar","age":24,"is_verified":True}
 
print(customer["name"])
print(customer["age"])

print(customer["is_verified"])

##### Example for dictionaies ######


phone = input("phone: ")
digi_num = {"1":"ONE","2":"Two","3":"three","4":"Four"}

output =""
for ch in phone:
    output += digi_num.get(ch, "!") + " "
print(output)







# In[10]:


######       Emoji Converter    #######

msg = input(">")
word = msg.split(' ')
emojis = {":)":"😊", ":(":"😒"}
output = ""
for dk in word:
    output += emojis.get(dk, dk) + " "
print(output)
    



 



# In[ ]:


#######     FuNction #######


 
    




