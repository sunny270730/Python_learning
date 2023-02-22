#!/usr/bin/env python
# coding: utf-8

# In[12]:


#### CREATE FUNCTION CONVERT NUMBER TO WORD   ######
def number_to_word(num):   
        ####   LIST STORE NUMBER 0-19 AND 20-90 ##
        words_0_to_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen','twenty']
        words_21_to_99 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
     #### LESS THEN 0 AND GREATER THEN 999 ### 
        if num < 0 or num > 999:
            return " number out of range (0-9999)."
       ###  NUM LESS THEN 20 #### 
        if num < 20:
            return words_0_to_20[num]
        ###### LIKE 20 TO 90 TAK NE DONO LIST CONBINE HOJAYE ####
        if num < 100:
            tens = words_21_to_99[(num // 10) - 2]
            ones = words_0_to_20[num % 10] 
            return tens + '-' + ones if num % 10 != 0 else tens  
    ##### LIKE 100 TO 999 HA TO ALL LIST COMBINE HOJAYE   #####
        if num < 1000:
            hundreds = words_0_to_20[num // 100] + ' hundred'
            tens = number_to_word(num % 100)
            return hundreds +  ' and '  + tens if num % 100 != 0 else hundreds
#### USER TO ENTER NUMBER  ####
num = input("Enter the number 0 to 999:- ")
####    CALL THE FUNCTION #####
if num.isdigit():
    word = number_to_word(int(num))
    print(word)
else:
    print('ERROR')

