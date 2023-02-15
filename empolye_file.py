#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

    
        

