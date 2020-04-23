from time import sleep
import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    todos.append(title)
    pass

def print_list():
    global todos
    print ("\n \n  THINGS TO DO: \n")
    lengthy =len(todos)
    for i in range (0,lengthy):
      print(str(i+1)+")"+ " "+ todos[i] + "\n")
      sleep(0.4)
    sleep(0.2)
    pass

def delete_task(number_to_delete):
    global todos
    lengthy =len(todos)
    number_as_int = int(number_to_delete)
    number_as_int = number_as_int - 1
    if (number_as_int <= lengthy):
    #  deleted_item = int(todos[number_as_int])
        print("... deleting item" +" "+ str(number_as_int+1))
        del todos[number_as_int]                # instead of del, would be more consistent with: todos.pop(int(number_to_delete))
    else:
        print("!! That item number exceeds the length of your list, try a lower number, please")
        sleep(1.4)
    sleep(0.6)
    print_list()
    pass

def save_todos():
    global todos
    myfile = open("todos.csv", "w")     # using W+ will overwrite, prefer not to use
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(todos)
    print ("saving...")
    sleep(0.33)
    pass

    
def load_todos():
    try:
        with open('todos.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Tasks are {", ".join(row)}')
                    sleep(2)
    except:
        print(" file not found")
        open("todos.csv", "w+")
        load_todos()

    
   
    ### 4Geeks method came out:
    # global todos
    # myfile = open("todos.csv","r")
    # csv_reader = csv.reader(myfile, quoting=csv.QUOTE.ALL)
    # for line in csv_reader:
    #       for task in line:
    #           todods = add_one_task(task)        


    # print(f'Processed {line_count} lines.')
    # pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    load_todos()

    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")