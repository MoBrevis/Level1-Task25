#   Creating a function that registers new users whose details are not yet in the text file.
def reg_user():
    print("\n----------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~| REGISTER |~~~~~~~~~~~~~~~~~~~~")
    print("----------------------------------------------------\n")

    with open("user.txt", "r") as file:
        file = open("user.txt", "r")
        for user_line in file:
            
            replace = user_line.replace("\n", "")
            split_list1 = replace.split(", ")
            read_list1.append(split_list1)

        file.close()

        validation = False

        while validation == False :
            
            new_user = input("Please enter your Username: ")

            for existing_user in read_list1:
                
                if new_user == existing_user[0]:            
                    print("Username already exists. Please try another username.")
                    break
                
            if new_user !=existing_user[0]:            
                new_password = input("Please enter your password: ")
                confirm_password = input("Please confirm your password: ")    
                            
                if confirm_password != new_password:            
                    print("The Password you have entered does not match, please try again!!")

                else:
                    file = open("user.txt", "a")
                    file.write("\n" + new_user + ", ")
                    file.write(confirm_password)
                    print("\n----------------------------------------------------")
                    print("~~~~~~~~~~| USERNAME AND PASSWORD CREATED |~~~~~~~~~")
                    print("----------------------------------------------------\n")
                    file.close()
                    return
                
#-------------------------------------------------------------------------------- END OF REGISTRATION FUNCTION ------------------------------------------------------------------------------

#   Creating a function that assigns a new task to the user and writes the details to a text file.        
def add_task():
    with open("tasks.txt") as file:
        print("\n----------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~~~| ADD TASKS |~~~~~~~~~~~~~~~~~y~~~")
        print("----------------------------------------------------\n")

        #   Opens tasks text file to append
        file = open("tasks.txt", "a")

        #   Requests user to input the following details
        username = (input("Please enter your username: "))
        title = (input("Please enter the title of the task: "))
        description = (input("Description of task: "))
        date_assigned = (input("Please enter the date assigned (format: year-month-day): "))
        due_date = (input("Please enter the due date (format: year-month-day): "))
        task_completed = ""

        #   Writes details to tasks text file
        file.write(username + ", " + title + ", " + description + ", " + date_assigned + ", " + due_date + ", " + task_completed + "\n")                
        print("\n----------------------------------------------------")
        print("~~~~~~~~~~~~~| TASK CREATED AND SAVED |~~~~~~~~~~~~~")
        print("----------------------------------------------------\n")
        file.close()
        return
    
#----------------------------------------------------------------------------------- END OF ADD TASK FUNCTION -------------------------------------------------------------------------------

#   Function that reads and convert data from tasks text file to a nested list.
def view_all_tasks():
    print("\n----------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~| VIEW ALL TASKS |~~~~~~~~~~~~~~~~~")
    print("----------------------------------------------------\n")

    for inner_list in list1:
        print("Assigned to: " + inner_list[0])
        print("Task Title: " + inner_list[1])
        print("Task Description: " + inner_list[2])
        print("Date assigned: " + inner_list[3])
        print("Due date: " + inner_list[4])
        print("Task complete?: " + inner_list[5])
        print()
        continue
    
#----------------------------------------------------------------------------------- END OF VIEW ALL TASK FUNCTION -------------------------------------------------------------------------

#   Creating a function that reads all the task assignments in the text file and  displays it in a user-friendly manner.
def view_my_tasks():
        print("\n----------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~| VIEW MY TASKS |~~~~~~~~~~~~~~~~~~")
        print("----------------------------------------------------\n")
        count = 1
        current_user = user
        group = []
        
        
        for group in list1:
            if  user == group[0]:
                print("Assigned to: " + group[0])
                print("Task Title: " + group[1])
                print("Task Description: " + group[2])
                print("Date assigned: " + group[3])
                print("Due date: " + group[4])
                print("Task complete?: " + group[5])
                print("Task number = " + str(count))
                print()
                count += 1
                
        file.close()
        return
    
#----------------------------------------------------------------------------------- END OF VIEW MY TASK FUNCTION ---------------------------------------------------------------------------

#   Function that enables the user to mark their task assignments as complete.
def mark_as_complete(x) :

    # Reading the files and importing them into lists.
    file = open("tasks.txt", "r")
    for task_line in file:
        replace = task_line.replace("\n", "")
        split_list2 = replace.split(", ")
        read_list2.append(split_list2)

    for group in read_list2:
        if  user == group[0]:
            read_list2[x - 1][5] = "Yes"
    file.close()
    
    return read_list2[x - 1], "Your task has been marked completed successful"

#----------------------------------------------------------------------------------- END OF SPECIFIC TASK FUNCTION --------------------------------------------------------------------------

#   Function that enables the user to edit their task. 
def edit_the_task(x):

    # Reading the files and importing them into lists.
    file = open("tasks.txt", "r")
    for task_line in file:
        replace = task_line.replace("\n", "")
        split_list2 = replace.split(", ")
        read_list2.append(split_list2)
     
    for group in read_list2:
        if  user == group[0]:
           username = input("Who is taking over the responsibility of this task: ")
           due = input("What is the new due date (format year-month-day): ")
           read_list2[x - 1][0] = username
           read_list2[x - 1][4] = due
           break
    file.close()
                    
    return read_list2[x - 1], "The editing of your details was successful"


#----------------------------------------------------------------------------------- LAST FUNCTION ------------------------------------------------------------------------------------

#   Function that writes the generated report to the task overview text file.
def my_function(num ,name) :

                
                u_over = ["The total number of users registered is " + str(stat_users), 
                "The total number of tasks that have been generated and tracked " + str(stat_task), 
                "The total number of tasks assigned to " + read_list2[name][0] + " is " + str(stat_task2), 
                "The percentage of the total number of tasks has been assigned to " + read_list2[name][0] + " is " + str(user_task_percentage) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " completed is " + str(com_task_percent) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " that must still be completed is " + str(incomplete_user_task) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " have not yet been completed and are overdue is " + str(percent_over_task) + "%"]

                return u_over[num]


def assign(num, name) :

    u_over = ["The total number of users registered is " + str(stat_users), 
                "The total number of tasks that have been generated and tracked " + str(stat_task), 
                "The total number of tasks assigned to " + read_list2[name][0] + " is " + str(stat_task2), 
                "The percentage of the total number of tasks has been assigned to " + read_list2[name][0] + " is " + str(user_task_percentage) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " completed is " + str(com_task_percent) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " that must still be completed is " + str(incomplete_user_task) + "%" ,
                "The percentage of the tasks assigned to " + read_list2[name][0] + " have not yet been completed and are overdue is " + str(percent_over_task) + "%"]
    
    return u_over

#----------------------------------------------------------------------------------- END OF FUNCTIONS ------------------------------------------------------------------------------------

# Greeting user to program.
print("----------------------------------------------------")
print("~~~~~~~| HELLO AND WELCOME TO TASK MANAGER! |~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~| LOGIN |~~~~~~~~~~~~~~~~~~~~~~")
print("----------------------------------------------------\n")

# Requesting a Username and Password.
print("Please enter your \n")
with open("user.txt", "r") as file:
    incorrect_info =  True
    while incorrect_info:
        user = input("username: ")
        
        file = open("user.txt", "r")

        for line in file:
            info = line.split(", ")
            if user == info[0]:
                break

        if user == info[0]:
            while True:
                password =  input("password: ")

                if password == info[1].strip():
                    incorrect_info = False
                    break

                else:
                    print("incorrect password, please try again")

        else:
            print("username does not exist")
        file.close()

    
#------------------------------------------------------------------------------------- END OF LOGIN ---------------------------------------------------------------------------------------

# Requesting user input from the menu.
menu = ""

while menu != "e":

    confirm_password: False
    admin = info[0]
    list1 = []
    list2 = []
    incomplete_tasks = 0
    complete_tasks = 0
    overdue_tasks = 0
    from datetime import date
    gen_rep = []
    stat_users = 0
    stat_task = 0
    stat_task2 = 0
    read_list1 =[]
    read_list2 =[]
    u_over_v2 = []
    
    print("\n----------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~| MENU |~~~~~~~~~~~~~~~~~~~~~~")
    print("----------------------------------------------------\n")
    
    # Menu display for the program when the user is not logged in.
    if user != "admin":

        print("Please select one of the following options below: " + "\n"+
        "\nr - register user (for Admin use only)" + "\n"+
        "a - add task" + "\n"+
        "va - view all tasks" + "\n"+
        "vm - view my tasks" + "\n"+
        "e - exit"+ "\n")
        menu = input("Menu option: ").lower()

    # Menu display for the program when the user is logged in.
    else:
        print("Please select one of the following options below: " + "\n" + "\n"+
        "r - register user" + "\n"+
        "a - add task" + "\n"+
        "va - view all tasks" + "\n"+
        "vm - view my tasks" + "\n"+
        "gr - generate reports" + "\n"+
        "ds - display statistics" + "\n"+
        "e - exit"+ "\n")
        menu = input("Menu option: ").lower()

    # Access the register and statics, only for admin use
    if user == "admin":
        
        # To register a new user.
        if menu == "r":

            reg_user()
            continue
            
        # To view the statistics of the program from users and tasks.  
        if menu == "ds":
            print("\n----------------------------------------------------")
            print("~~~~~~~~~~~~~~~| DISPLAY STATISTICS |~~~~~~~~~~~~~~~")
            print("----------------------------------------------------\n")

            # Reading the files and importing them into lists.
            file = open("user.txt", "r")
            for user_line in file:
                replace = user_line.replace("\n", "")
                split_list1 = replace.split(", ")
                read_list1.append(split_list1)

            for items in read_list1:
                if items[0] != "":
                    stat_users += 1
                

            file = open("tasks.txt", "r")
            for task_line in file:
                replace = task_line.replace("\n", "")
                split_list2 = replace.split(", ")
                read_list2.append(split_list2)
            #   The total number of tasks that have been generated and tracked using the task_manager.py .                
            for items in read_list2:                    
                if items[1] != "":
                    stat_task += 1
                    
            
            # Output the statistics
            print("The total number of users is {} (Incl Admin)".format(stat_users))
            print("The total number of tasks is {}".format(stat_task))
            file.close()
            continue
#------------------------------------------------------------------------------------------ End of Statistics -------------------------------------------------------------------------------        
        #   Generates user and task reports            
        if menu == "gr":
            print("\n----------------------------------------------------")
            print("~~~~~~~~~~~~~~~~| GENERATE REPORTS |~~~~~~~~~~~~~~~~")
            print("----------------------------------------------------\n")

            print("\n----------------------------------------------------")
            print("~~~~~~~~~~~~~~~~~~| TASK OVERVIEW |~~~~~~~~~~~~~~~~~")
            print("----------------------------------------------------\n")

            file = open("user.txt", "r")
            for user_line in file:
                replace = user_line.replace("\n", "")
                split_list1 = replace.split(", ")
                read_list1.append(split_list1)

            for items in read_list1:
                if items[0] != "":
                    stat_users += 1
                

            file = open("tasks.txt", "r")
            for task_line in file:
                replace = task_line.replace("\n", "")
                split_list2 = replace.split(", ")
                read_list2.append(split_list2)
                
            #   The total number of tasks that have been generated and tracked using the task_manager.py .                
            for items in read_list2:                    
                if items[1] != "":
                    stat_task += 1        
                
                    
            #   The total number of completed tasks.
            for items in read_list2:
                if items[5] == "Yes":
                    complete_tasks += 1
                    
            #   The total number of uncompleted tasks and the percentage of tasks that are incomplete.
            for items in read_list2:
                if items[5] != "Yes":
                    incomplete_tasks += 1
                    percentage = ((incomplete_tasks / stat_task)*100)
                    perc_incomplete_tasks = round(percentage)
                    
            #   The total number of tasks that haven’t been completed and that are overdue. Also the percentage of tasks that are overdue.
            for items in read_list2:
                if items[5] != "Yes":
                    if items[4] != "":
                        items = items[4].replace("-","")
                        today = date.today()
                        items2 = (str(today).replace("-",""))

                        if int(items) < int(items2):
                            overdue_tasks +=1
                            
                            percent_over = ((overdue_tasks / stat_task)*100)
                            percent_over_task = round(percent_over)

            file = open("task_overview.txt", "r+")
            gen_rep = ["The total number of tasks is " + str(stat_task) ,
                   "The total number of completed tasks is " + str(complete_tasks) ,
                   "The total number of uncompleted tasks is " + str(incomplete_tasks) ,
                   "The total number of tasks that haven’t been completed is " + str(incomplete_tasks)  + " and that are overdue " + str(overdue_tasks) ,
                   "The percentage of tasks that are incomplete is " + str(perc_incomplete_tasks) + "%" ,
                   "The percentage of tasks that are overdue is " + str(percent_over_task) + "%"]
            
            for i in gen_rep :
                print(i)
                file.write(i + "\n")

            file.close()
                
            print("\n----------------------------------------------------")
            print("~~~~~~~~~~~~~~~~~~| USER OVERVIEW |~~~~~~~~~~~~~~~~~")
            print("----------------------------------------------------\n")

            stat_users = 0
            stat_task = 0
            stat_task2 = 0
            read_list1 =[]
            read_list2 =[]

#----------------------------------------------------------------------------------------- reading file ------------------------------------------------------------------------------------
            file = open("user.txt", "r")
            for user_line in file:
                replace = user_line.replace("\n", "")
                split_list1 = replace.split(", ")
                read_list1.append(split_list1)

            for items in read_list1:
                if items[0] != "":
                    stat_users += 1

            file = open("tasks.txt", "r")
            for task_line in file:
                replace = task_line.replace("\n", "")
                split_list2 = replace.split(", ")
                read_list2.append(split_list2)
                
            #   The total number of tasks that have been generated and tracked using the task_manager.py .                
            for items in read_list2:                    
                if items[1] != "":
                    stat_task += 1
#-------------------------------------------------------------------------------------- End of reading file ---------------------------------------------------------------------------------                        
            # The total number of tasks assigned to that specific user.
            for items in read_list2:
                if items[0]:
                    if items[1] !=  "":
                        stat_task2 += 1

            # What percentage of the total number of tasks have been assigned to that user?
            user_task_percent = ((stat_task2 / stat_task)*100)
            user_task_percentage = round(user_task_percent)

            # What percentage of the tasks assigned to that user have been completed?
            for items in read_list2:
                if items[0]:
                    if items[5] == "Yes":
                        complete_tasks += 1
                        com_task_percentage = ((complete_tasks / stat_task2)*100)
                        com_task_percent = round(com_task_percentage)

            # What percentage of the tasks assigned to that user must still be completed?
            if items[0]:
                incomplete = ( (stat_task2-complete_tasks) / stat_task2) * 100
                incomplete_user_task = round(incomplete)

            # What percentage of the tasks assigned to that user have not yet been completed and are overdue?
            for items in read_list2:
                if items[0]!=  "":
                    if items[5] != "Yes":
                        if items[4] != "":
                            items = items[4].replace("-","")
                            today = date.today()
                            items2 = (str(today).replace("-",""))

                            if int(items) < int(items2):
                                overdue_tasks +=1                            
                                percent_over = ((overdue_tasks / stat_task2)*100)
                                percent_over_task = round(percent_over)

            file = open("user_overview.txt", "r+")

            file.write("Total number of registered users = " + str(stat_users) + "\nTotal number of tasks = " + str(stat_task) + "\n")
            file.write("\n")
            
            for group in read_list2:
                if group[0] != "":
                    user_over = [group[0] + ":" ,
                        "Percentage of tasks assigned is " + str(user_task_percentage)+ "%" , 
                        "Percentage of completed tasks is " + str(complete_tasks) + "%" , 
                        "Percentage of incompleted tasks is " + str(incomplete_user_task) + "%" , 
                        "Percentage of tasks that are incomplete and overdue is " + str(percent_over_task) + "%\n"]

            for i in user_over:
                print(i)
                file.write(i + "\n")
                        

            file.close()
            
            continue      


#--------------------------------------------------------------------------------------- End of Reports -------------------------------------------------------------------------------------
                
    # User selected to input new tasks.
    if menu == "a":
        add_task()
        continue
    
#--------------------------------------------------------------------------------------- End of Add task -------------------------------------------------------------------------------------

    # Reading the files and importing them into lists.    
    file = open("tasks.txt", "r")

    read_list = []

    for line in file :
        line = line[:-1]
        read_list.append(line)

    file.close()

    list1 = []

    for string in read_list :
        space = string.replace("\n", "")
        string_to_list = space.split(", ")
        list1.append(string_to_list)
    

    # User selected to view all tasks, display the information for each task on the screen in an easy to read format.    
    if menu == "va":
        view_all_tasks()
        continue
        
    # User selected to view my tasks, to view the tasks that are assigned to them. 
    # Only display all the tasks that have been assigned to the user that is currently logged-in in a user-friendly, easy to read manner.
    if menu == "vm":

        view_my_tasks()

        user_choice1 = int(input("Which task number you'd like to select: "))
        user_choice2 = input("Would you like to mark as complete or edit: ")
        
        if user_choice2 == "mark as complete":
            print(mark_as_complete(user_choice1))
            
        elif user_choice2 == "edit":
            print(edit_the_task(user_choice1))
        continue    
#--------------------------------------------------------------------------------------- End of VA and VM -----------------------------------------------------------------------------------
    # Access to register users only allowed to admin.  
    if menu == "r":
        print("\n----------------------------------------------------")
        print("~~~~~~~| ACCESS DENIED. FOR ADMIN USE ONLY. |~~~~~~~")
        print("----------------------------------------------------\n")
        continue
    
    # if nothing has been entered to give an error message.
    if menu == "":
        print("\n----------------------------------------------------")
        print("~ YOU HAVE NOT ENTERED ANYTHING. PLEASE TRY AGAIN! ~")
        print("----------------------------------------------------\n")
        continue
    
    # this function is to exit the program
    if menu == "e":
        print("\n----------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~~~~| GOOD BYE |~~~~~~~~~~~~~~~~~~~~")
        print("----------------------------------------------------\n")

