#!/usr/bin/env python
# coding: utf-8

# In[20]:


employees = []  # list to store all employee data

while True:
    print("Press 1 to enter employee data")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
 ###### Read employee data from keyboard   ######
        emp_no = input("Employee No: ")
        emp_name = input("Employee Name: ")
        emp_salary = float(input("Employee Salary: "))
        emp_address = input("Employee Address: ")
        emp_married = input("Employee Married? (True/False): ")
        emp_married = True if emp_married.lower() == "true" else False

       ###### create dictionary of employee data #######
        emp_data = {
            "Employee No": emp_no,
            "Employee Name": emp_name,
            "Employee Salary": emp_salary,
            "Employee Address": emp_address,
            "Employee Married": emp_married
        }

        ######## add dictionary to list of employees   #########
        employees.append(emp_data)
        print("employee married confirm ")
           
       ########## prompt to add another user ############
        add_emp = input("(yes/y or no/n): ")
        if add_emp.lower() in ["no", "n"]:
            break

    elif choice == "2":
        break

    else:
        print("no data employeee")

######### display all employee information  ########
print("All Employee Information:")

for emp in employees:
    print(emp)

######## store the result in a file   ##########
with open("employees.txt", "w") as file:
    for emp in employees:
        file.write(str(emp) + "\n")
print("Employee data stored in employees.txt file.")


# In[ ]:





# In[ ]:




