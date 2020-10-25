
#.  Each entry in the database is described by four attributes: student number (integer), student name (a string), GPA (float), and major (string).

dict = {}

def readdatafile():
    while(True):
        filename = input('Enter the filename: ')

        try:
            f = open(filename, 'r').readlines()
        except FileNotFoundError:
            print("Wrong file name....Try Again!!!\n")
        else:
            break

    f = open(filename, 'r')
    lines = f.readlines()

    for line in lines:
        data1 = line.split()

        sid, name, gpa, major = data1
        dict[int(sid)] = [name, float(gpa), major]

    print("\nData from file saved to database!!!")
    print('----------------------------------------')
    f.close()

def writetofile():
    f = open("pythonln.txt", "w")

    for i in sorted(dict.keys()):
        list1 = dict[i]
        f.write(str(i) + ' ' + list1[0] + ' ' + str(list1[1]) + ' ' + list1[2] + '\n')
    f.close()
    print("\nOutput File has been updated successfully!!!")

def getstudentbyid(sid):
    l1 = dict.get(sid)

    if l1:
        print("\n____________Student-Info___________")
        print("     Student Name : " + l1[0])
        print("     Student Gpa  : ", l1[1])
        print("     Student Major: "+ l1[2])
        print('-------------------------------------')
    else:
        print('\nStudent with Id: ', sid,' not found in database.')

def getallstudents():

    while(True):
        print('\n---------------------------------------------------')
        print('1. Sort by SID')
        print('2. Sort by GPA')
        num = int(input('Select an option from above and enter its number > '))

        if num == 1:
            list1 = []
            print("\nStudent: Information by ID")
            print('----------------------------- ')
            for i in sorted(dict.keys()):
                list1 = dict[i]
                print('ID: ', i , '| Name: ' + list1[0] + '| GPA: ', list1[1] , '| Major: ' + list1[2])
            break

        elif num == 2:
            list2 = []
            print("\nStudent: Information by GPA")
            print('-------------------------------')
            for value in dict.values():
                tup = (value[1], value[0], value[2])
                list2.append(tup)
            ls = sorted(list2)

            for i in ls:
                print(' GPA: ', i[0] , '| Name: ' + i[1] + '| Major: ' + i[2])
            break

        else:
            print('You entered a wrong option. Try Again!!!\n')


def addstudent():

    sid = int(input('Enter Student ID: '))
    l1 = dict.get(sid)

    if l1:
        print('\nStudent ID: ', sid , ' already present in DataBase')
    else:

        while True:
            try:
                data1 = input('Enter Student Name , Gpa and Major: ')
                name, gpa, major = data1.split()
                break
            except ValueError:
                print("\nOops! Invalid Entry Try again...")

        dict[sid] = [name, float(gpa), major]
        print('\n' + name + ', with SID ', sid, ' successfully added to database. ' + 'GPA: ', gpa, ' and Major: ' + major)

def findhighestgpa():
    highest_gpa = 0.0
    name = ''
    major = ''

    for value in dict.values():
        stugpa = value[1]
        if stugpa > highest_gpa:
            highest_gpa = stugpa
            name = value[0]
            major = value[2]
        elif stugpa == highest_gpa:
            highest_gpa = highest_gpa

    print('\nStudent with highest GPA')
    print('----------------------------')
    print('Student Name : ' + name)
    print('Student GPA  : ', highest_gpa)
    print('Student Major: ' + major)
    print('----------------------------\n')

def findaveragegpa():
    count = 0;
    sum = 0;
    for value in dict.values():
        sum += value[1]
        count += 1

    print('\nAverage GPA of all students: ', round(sum/count,2))

readdatafile()

while(True):
    print('\nWelcome to Student DataBase Management System')
    print('----------------------------------------------')
    print('               Main Menu')
    print('----------------------------------------------')
    print('1. Retrieve Data (for a given SID)')
    print('2. Display database sorted by SID or GPA')
    print('3. Add student')
    print('4. Find highest GPA (of all students)')
    print('5. Find average GPA (of all students)')
    print('6. Terminate \n')

    option = int(input('Select an option from the menu and enter its number > '))

    if option == 1:
        id = int(input("Enter id to view student info: "))
        getstudentbyid(id)
    elif option == 2:
        getallstudents()
    elif option == 3:
        addstudent()
    elif option == 4:
        findhighestgpa()
    elif option == 5:
        findaveragegpa()
    elif option == 6:
        writetofile()
        print('You choose to Terminate the Program')
        break
    else:
        print('Enter a valid option from the main menu!!!')

    keyboard_enter = input("\n Press ENTER to view main menu options!!!")
    if keyboard_enter == '':
        continue









