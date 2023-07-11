import mysql.connector

def view_managers(mycursor):
    while True:
        choice = input("Enter region name for specific region or (All) to view all regions: ")
        if (choice != ""):
            break
        else:
            print("ERROR: You must input a value at the prompt.")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query = "SELECT * FROM EmployeesPerRegion"
    else:
        query= "SELECT * FROM EmployeesPerRegion WHERE region_name = '{}';".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no employees in {choice} region")
    else:
        for record in query_result: 
            print(f"{record[0]}:{record[1]}")
    
def managersPerDepartment(mycursor):
    while True:
        choice = input("Enter department name for specific department or (All) to view all departments: ")
        if (choice != ""):
            break
        else:
            print("ERROR: You must input a value at the prompt.")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query = "SELECT department_name, COUNT(email) FROM managers GROUP BY department_name;"
    else:
        query = "SELECT department_name, COUNT(email) FROM managers WHERE department_name LIKE '%{}%' GROUP BY department_name;".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no departments named {choice}.")
    else:
        for record in query_result:
            print(f"{record[0]} Department: {record[1]} managers")
def mostDependents(mycursor):
    while True:
        choice = input("Enter department name for specific department or (All) to view all departments: ")
        if (choice != ""):
            break
        else:
            print("ERROR: You must input a value at the prompt.")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query = "SELECT department_name,NumOfDependents FROM DependentsByDepartment;"
    else:
        query = "SELECT department_name,NumOfDependents FROM DependentsByDepartment WHERE department_name = '{}';".format(choice) 
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no departments named {choice}.")
    else:
        for record in query_result:
            print(f"{record[0]} : {record[1]} dependents")

def hiresByYear(mycursor):
    while True:
        choice = input("Enter year or (All) to view hiring data for all years: ")
        if (choice != ""):
            break
        else:
            print("Error: You must input a value at the prompt")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query = "SELECT * FROM HiresByYear;"
    else:
        query = "SELECT * FROM HiresByYear WHERE year = '{}';".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no hires in the year {choice}")
    else:
        for record in query_result:
            print(f"{record[0]} : {record[1]} hires")

def salaryByDepartment(mycursor):
    while True:
        choice = input("Enter department name for specific department or (All) to view all departments: ")
        if(choice !=""):
            break
        else:
            print("Error: You must input a value at the prompt")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query="SELECT * FROM SalaryByDepartment;"
    else:
        query = "SELECT * FROM SalaryByDepartment WHERE department_name = '{}';".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no salaries for {choice}")
    else:    
        for record in query_result:
            print(f"{record[0]} : {record[1]}")

def salaryByJobTitle(mycursor):
    while True:
        choice = input("Enter job title for specific job title or (All) to view all job titles: ")
        if (choice != ""):
            break
        else:
            print("Error: You must input a value at the prompt")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query="SELECT * FROM SalaryByJobTitle;"
    else:
        query="SELECT * FROM SalaryByJobTitle WHERE job_title = '{}'".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no salaries for {choice}")
    else:
        for record in query_result:
            print(f"{record[0]} : ${record[1]}")

def employeeDependents(mycursor):
    while True:    
        choice = input("Enter employee first name and last name or (All) to see dependents data for employee(s): ")
        if(choice != ""):
            break
        else:
            print("Error: You must input a value at the prompt")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query="SELECT * FROM EmployeeDependents;"
    else:
        query="SELECT first_name, last_name, numOfDependents FROM EmployeeDependents WHERE first_name = '{}';".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no employees named {choice}")    
    else:    
        for record in query_result:
            print(f"{record[0]} {record[1]}: {record[4]} dependents.")

def countryLocation(mycursor):
    while True:    
        choice = input("Enter employee first name and last name or (All) to see dependents data for employee(s): ")
        if(choice != ""):
            break
        else:
            print("Error: You must input a value at the prompt")
    if (choice == "all" or choice == "ALL" or choice == "All"):
        query="SELECT * FROM CountryLocation;"
    else:
        query="SELECT * FROM CountryLocation WHERE country_name = '{}';".format(choice)
    mycursor.execute(query)
    query_result = mycursor.fetchall()
    if not query_result:
        print(f"There are no locations named {choice}")    
    else:    
        for record in query_result:
            print(f"{record[0]}: {record[2]} locations")

def addDepen(mycursor,mydb):
    first = input("Enter dependent first name: ")
    last = input("Enter dependent last name: ")
    child = input("What is the dependents relationship: ")
    while True:
        try:
            empId = int(input("Enter employee id number of dependent: "))
        except:
            print("Error: Employee id incorrect.")
            continue
        else:
            break
    child = input("What is the dependents relationship?")
    query = "INSERT INTO dependents (dependent_id,first_name,last_name,relationship,employee_id) SELECT MAX(dependent_id) + 1, '{}','{}','{}','{}' FROM dependents;".format(first,last,"Child",empId)
    mycursor.execute(query)
    mydb.commit()

def addJob(mycursor, mydb):
    title = input("Enter job title: ")
    while True:
        try:
            min = float(input("Enter minimum salary: "))
        except:
            print("Error: Enter a number.")
            continue
        else:
            break
    while True:
        try:
            max = float(input("Enter maximum salary: "))
        except:
            print("Error: Enter a number.")
            continue
        else:
            break
    query = "INSERT INTO jobs (job_id,job_title,min_salary,max_salary) SELECT MAX(job_id) + 1, '{}','{}','{}' FROM jobs;".format(title,min,max)
    mycursor.execute(query)
    mydb.commit()
def delEmp(mycursor,mydb):
    while True:
        try:
            empId = int(input("Enter employee id number to delete: "))
        except:
            print("Error: Employee id incorrect.")
            continue
        else:
            break
    query = "DELETE FROM employees WHERE employee_id = '{}'".format(empId)
    mycursor.execute(query)
    mydb.commit()
def delDepen(mycursor,mydb):
    while True:
        try:
            depId = int(input("Enter dependent id number to delete: "))
        except:
            print("Error: Dependent id incorrect.")
            continue
        else:
            break
    query = "DELETE FROM dependents WHERE dependent_id = '{}'".format(depId)
    mycursor.execute(query)
    mydb.commit()
def updateFirst(mycursor,mydb):
    while True:
        try:
            empId = int(input("Enter employee id number to change name: "))
        except:
            print("Error: Employee id incorrect.")
            continue
        else:
            break
    name = input("Enter employees new name: ")
    query = "UPDATE employees SET first_name = '{}' WHERE employee_id = '{}'".format(name,empId)
    mycursor.execute(query)
    mydb.commit()
def updateLast(mycursor,mydb):
    while True:
        try:
            empId = int(input("Enter employee id number to change last name: "))
        except:
            print("Error: Employee id incorrect.")
            continue
        else:
            break
    name = input("Enter employees new last name: ")
    query = "UPDATE employees SET last_name = '{}' WHERE employee_id = '{}'".format(name,empId)
    mycursor.execute(query)
    mydb.commit()
def updateMin(mycursor,mydb):
    while True:
        try:
            jobId = int(input("Enter job id number to change minimum salary: "))
        except:
            print("Error: Job ID incorrect.")
            continue
        else:
            break
    while True:
        try:
            min = float(input("Enter minimum salary: "))
        except:
            print("Error: Salary incorrect.")
            continue
        else:
            break
    query = "UPDATE jobs SET min_salary = '{}' WHERE job_id = '{}'".format(min,jobId)
    mycursor.execute(query)
    mydb.commit()
def updateMax(mycursor,mydb):
    while True:
        try:
            jobId = int(input("Enter job id number to change maximum salary: "))
        except:
            print("Error: Job ID incorrect.")
            continue
        else:
            break
    while True:
        try:
            max = float(input("Enter maximum salary: "))
        except:
            print("Error: Salary incorrect.")
            continue
        else:
            break
    query = "UPDATE jobs SET max_salary = '{}' WHERE job_id = '{}'".format(max,jobId)
    mycursor.execute(query)
    mydb.commit()

def print_menu():
    print("\nChoose an option")
    print("-------------------------------------\n")
    print("---------- VIEW DATA ----------\n")
    print("1. View employees data per region")
    print("2. View number of managers in each department")
    print("3. View manager count by department")
    print("4. View hiring data by year")
    print("5. View salary data by department")
    print("6. View salary data by job title")
    print("7. View dependent data by employee")
    print("8. View location data by country")
    print("\n---------- ADD DATA ----------\n")
    print("9. Add a dependent")
    print("10. Add a job")
    print("\n ---------- DELETE DATA ----------\n")
    print("11. Delete an employee")
    print("12. Delete a dependent")
    print("\n---------- UPDATE DATA ----------\n")
    print("13. Update employee first name")
    print("14. Update employee last name")
    print("15. Update job minimum salary")
    print("16. Update job maximum salary")
    print("\n---------- EXIT ----------\n")
    print("17. Exit Application")
    return

def get_user_choice():
    while True:    
        print_menu()
        choice = input("Enter Choice: ")   
        try:    
            choice = int(choice)
            if(choice <1 or choice > 17):
                print("\nError: Enter a number between 1-17")
                continue
        except:
            print("\nError enter a number.")
            continue
        else:    
            return choice

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        user_choice = get_user_choice()
        if(user_choice == 1):
            #call the function to query the managers
            view_managers(mycursor)
        elif(user_choice == 2):
            managersPerDepartment(mycursor)
        elif(user_choice==3):
            mostDependents(mycursor)
        elif(user_choice==4):
            hiresByYear(mycursor)
        elif(user_choice==5):
            salaryByDepartment(mycursor)
        elif(user_choice==6):
            salaryByJobTitle(mycursor)
        elif(user_choice==7):
            employeeDependents(mycursor)
        elif(user_choice==8):
            countryLocation(mycursor)
        elif(user_choice==9):
            addDepen(mycursor,mydb)
        elif(user_choice==10):
            addJob(mycursor,mydb)
        elif(user_choice==11):
            delEmp(mycursor,mydb)
        elif(user_choice==12):
            delDepen(mycursor,mydb)
        elif(user_choice==13):
            updateFirst(mycursor,mydb)
        elif(user_choice==14):
            updateLast(mycursor,mydb)
        elif(user_choice==15):
            updateMin(mycursor,mydb)
        elif(user_choice==16):
            updateMax(mycursor,mydb)
        elif(user_choice == 17):
            print("Bye Bye!!!")
            break

main()
