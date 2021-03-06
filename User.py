try:
    import mysql.connector as sqltor
    import PySimpleGUI as sg
    import os
    import webbrowser
    import matplotlib.pyplot as plt
    from googlesearch import search

except ImportError:
    import sys, subprocess
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", 'matplotlib'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'google'])
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", 'PySimpleGUI'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'mysql-connector-python'])
    import PySimpleGUI as sg
    import mysql.connector as sqltor
    import os
    import webbrowser
    import matplotlib.pyplot as plt
    from googlesearch import search

# Error handling for importing modules

sg.theme('BluePurple')

# To set theme of window
filename = "temp.txt"
if os.path.isfile(filename):

    # Checking for previously saved passwords

    file = open(filename, "r")
    string = file.readline()
    user = string.split(":")[1]
    string = file.readline()
    password = string.split(":")[1]
    mycon = sqltor.connect(user=user, password=password, host='localhost')
    mycur = mycon.cursor()
    file.close()
else:

    # Taking input for username and password and connecting to MySQL server

    layout = [[sg.Text(text="Enter Mysql Login Credentials")],

              # Layout for window

              [sg.Text(text="Username"),
               sg.In(default_text='root', key='username')],
              [sg.Text(text="Password"),
               sg.In(password_char='*', key='password')],
              [sg.Button(button_text='Login', key='login'),
               sg.Button(button_text='Cancel', key="Cancel")],
              [sg.Text(text="Save Password?"),
               sg.Radio("Yes", "radio1", key='--SAVE--'),
               sg.Radio("No", "radio1", default=True)],
              [sg.Text(key='label', text='', size=(60, 1))]]
    window1 = sg.Window(title='MYSQL Login Page', layout=layout)

    # Using PySimpleGUI to create user interface for entering sql credentials

    while True:
        event, value = window1.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':

            # For closing the window

            quit()
        elif event == 'login':
            user = value['username']
            password = value['password']
            if value['--SAVE--']:
                # if user wants to save password

                with open(filename, "w") as file:
                    file.write("User:" + user + "\nPassword:" + password)
            try:
                mycon = sqltor.connect(user=user, password=password,
                                       host='localhost')
                mycur = mycon.cursor()
                if mycon.is_connected():
                    break
            except (sqltor.ProgrammingError, sqltor.OperationalError) as e1:
                window1.FindElement('label').Update(
                    "Can't connect to server, Check server status and credentials")

        # error handling for SQL Login

    window1.close()
RightColumn = [[sg.Text(text="Create Users Here", )],
               [sg.Text(text='Enter Name'),
                sg.In(default_text='ABCD', text_color='black', key='name')],
               [sg.Text(text='Enter Phone'),
                sg.In(default_text='1234567890', text_color='black',
                      key='phone')],
               [sg.Text(text='Enter Address'),
                sg.In(default_text='H-1892', text_color='black',
                      key='address')],
               [sg.Text(text="Covid Status"),
                sg.Radio(text="+ve", key='+ve', group_id="radio1"),
                sg.Radio(text="-ve", key="-ve", group_id="radio1",
                         default=True)],
               [sg.Button(button_text='Submit', key='submit', pad=(70, 0))],
               [sg.Button(button_text="Update", key='Update', pad=(70, 10))],
               [sg.Text(text='', size=(40, 1), key="UserError")]]

# Layout of row 1 column 2 for creating new users
menulayout = [["Options", ["Clear Database", "Delete Saved Password"]],
              ["Help", ["About...", "Help"]]]
leftColumn = [[sg.Text(text="Find Users Here")],
              [sg.Text(text='Search User By'),
               sg.InputOptionMenu(values=['UserID', 'Name', 'Address', 'Phone',
                                          'CovidStatus'], key="option")],
              [sg.Text(text="Enter the query"), sg.In(key='squery'),
               sg.Button(button_text='Search', key='search')],
              [sg.Table(headings=["UserID", "Name", "Phone", "Address",
                                  "CovidStatus"],
                        values=[("UID", " SAMPLE ", "1234567890", "VWXYZ",
                                 "-ve"), ],
                        enable_events=True, key="list", size=(300, 10),
                        pad=(70, 10))], ]

# Layout of row 1 column 1 for searching existing users

DisabledLeftColumn = [[sg.Text(text='Update'),
                       sg.InputOptionMenu(
                           values=['---', "Name", "Phone", "Address",
                                   "CovidStatus"], key="l3option",
                           default_value='---')],
                      [sg.Text("Enter UserID"), sg.In(key="UQuery")],
                      [sg.Text('Enter New Value'), sg.In(key="NValue")],
                      [sg.Button("Update", key="update"),
                       sg.Button(button_text="Back to Create Users",
                                 key="return")],
                                 [sg.Button('Delete',k='delete')]]

# Layout of row 1 column 2 (not visible untill update button is pressed) for updating info of existing users

LeftColumn1 = [[sg.Text(text="Log Meetings Here", pad=(10, 0))],
               [sg.Text(text='Enter UserIDs'),
                sg.In(default_text='1,2,4', text_color='black', key='UIs')],
               [sg.Text(text="Enter Date    "),
                sg.In(default_text='yyyy-mm-dd', text_color='black',
                      key='Date')],
               [sg.Text(text="Enter Purpose"),
                sg.InputOptionMenu(
                    values=["Friend/Family", "Business", "Service and Repair",
                            "Other"],
                    key="purpose")],
               [sg.Button(button_text='Submit', key='Submit')],
               [sg.Text(text='', key="MeetError", size=(40, 1))]]

# Layout of row 2 column 1 for logging meetings of users

RightColumn1 = [
    [sg.Button("COVID test centre near me", k="hospitallist", pad=(20, 10))],
    [sg.Text('To view block wise'),
    sg.Button('View graph', k="graph")]]

layout2 = [[sg.Menu(menulayout)],
           [sg.Column(leftColumn),
            sg.VSeperator(color="lightblue", pad=(0, 0)),
            sg.Column(RightColumn, key="CreateUser"),
            sg.Column(DisabledLeftColumn, visible=False, key="UpdateUser")],
           [sg.HorizontalSeparator(color="lightblue", pad=(0, 10))],
           [sg.Column(LeftColumn1),
            sg.VSeperator(color="lightblue", pad=(0, 0)),
            sg.Column(RightColumn1)]]

# Layout for entire window (window2)

window2 = sg.Window(title="COVID19 User Finder/Creator", layout=layout2)
while True:
    dbuse = 'use covid19;'
    event, value = window2.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Submit':

        # This checks for existing database (covid19). If it does not exist, it creates one

        mycur.execute("show databases;")
        data = mycur.fetchall()
        if ('covid19',) in data:
            mycur.execute(dbuse)
        else:
            mycur.execute("create database covid19;")
            mycur.execute(dbuse)
        mycur.execute("show tables")
        data = mycur.fetchall()
        if ('meetinginfo',) in data:
            # Checks for existing table (MeetingInfo). If it does not exist, it creates one
            try:
                mycur.execute(
                    "insert into meetinginfo(Purpose,Date) values('%s','%s');" % (
                    value['purpose'], value['Date']))

                # inserts values entered by user into the  table

                mycur.execute("select max(MeetId) from MeetingInfo")
                (MeetId,) = mycur.fetchone()
                uid = value['UIs']
                uidlist = [(MeetId, UserID) for UserID in uid.split(',')]
                mycur.executemany(
                    "insert into MeetingUser(MeetId,UserId) values(%s,%s)",
                    uidlist)
                # Insterts value into the table (MeetingUser)
                window2.FindElement("MeetError").Update('')
                mycon.commit()
            except sqltor.Error:
                window2.FindElement("MeetError").Update(
                    "There was a problem logging the meet")

            mycur.execute(
                'select m.meetid  from meetinguser m,user n where m.userid=n.userid and n.covidstatus="+ve"')
            data = mycur.fetchall()

            # Selecting meeting IDs of meetings in which covid +ve person was there

            data = [i for (i,) in data]
            temp = []
            for i in range(len(data)):
                mycur.execute(
                    "select m.userid from meetinguser m , user n where m.userid=n.userid and m.meetid=%s" %
                    data[i])
                temp.append(mycur.fetchall())

            # Selecting user IDs of the the people attending the meetings in which a covid patient was there

            mycur.execute("select userid from user where covidstatus='+ve'")
            surecases = mycur.fetchall()
            surecases = [j for (j,) in surecases]
            temp2 = []
            for i in temp:
                for (j,) in i:
                    temp2.append(j)
            temp = temp2
            try:
                for i in surecases:
                    temp.remove(i)
            except ValueError:
                pass
            # Removing those who have been tested +ve for covid

            for i in temp:
                mycur.execute(
                    "update user set covidstatus='prob+ve' where (userid=%s and covidstatus='-ve')" % i)

                # Setting covid status of people who attended meeting with covid patient to prob+ve
            mycon.commit()
        else:
            mycur.execute(
                "create table MeetingInfo(MeetId int primary key auto_increment,"
                "Purpose varchar(20) not null,"
                "Date Date not null);")

            # Creates table (MeetingInfo)

            mycur.execute("create table MeetingUser(MeetId int not null ,"
                          "UserId int not null,"
                          "foreign key(MeetId) references MeetingInfo(MeetId),"
                          "foreign key (UserId) references user(UserId));")

            # Creates table (MeetingUser)

            try:
                mycur.execute(
                    "insert into meetinginfo(Purpose,Date) values('%s','%s');" % (
                    value['purpose'], value['Date']))

                # inserts values entered by user into the  table

                mycur.execute("select max(MeetId) from MeetingInfo")
                for i in mycur.fetchone():
                    MeetId = i
                uid = value['UIs']
                uidlist = [(MeetId, UserID) for UserID in uid.split(',')]
                mycur.executemany(
                    "insert into MeetingUser(MeetId,UserId) values(%s,%s)",
                    uidlist)
                # Insterts value into the table (MeetingUser)
                mycon.commit()
            except sqltor.Error:
                window2.FindElement("MeetError").Update(
                    "There was a problem logging the meet")

            # Insterts value into table(MeetingUser)

            mycon.commit()
            mycur.execute('select m.meetid  from meetinguser m,user n '
                          'where m.userid=n.userid and n.covidstatus="+ve";')
            data = mycur.fetchall()

            # Selecting meeting IDs of meetings in which covid +ve person was there

            data = [i for (i,) in data]
            temp = []
            for i in range(len(data)):
                mycur.execute(
                    "select m.userid from meetinguser m , user n "
                    "where m.userid=n.userid and m.meetid=%s" % data[i])
                temp.append(mycur.fetchall())

            # Selecting user IDs of the the people attending the meetings in which a covid patient was there

            mycur.execute("select userid from user where covidstatus='+ve'")
            surecases = mycur.fetchall()
            surecases = [j for (j,) in surecases]
            temp2 = []
            for i in temp:
                for (j,) in i:
                    temp2.append(j)
            temp = temp2
            try:
                for i in surecases:
                    temp.remove(i)
            except ValueError:
                pass
            # Removing those who have been tested +ve for covid

            for i in temp:
                mycur.execute(
                    "update user set covidstatus='prob+ve' where (userid=%s and covidstatus='-ve')" % i)

                # Setting covid status of people who attended meeting with covid patient to prob+ve

            mycon.commit()


    elif event == 'submit':

        # To create new users

        mycur.execute("show databases;")
        data = mycur.fetchall()
        if ('covid19',) in data:
            mycur.execute(dbuse)
        else:
            mycur.execute("create database covid19;")
            mycur.execute(dbuse)

        # Checking for database covid 19 and if it doesn't exist, it creates one

        mycur.execute("show tables")
        data = mycur.fetchall()
        if ('user',) in data:

            # Checks if the table User exists or not and if it doesn't exist, it creates one

            try:
                r_keys = ["+ve", "-ve"]
                mycur.execute(
                    "insert into User(Name,Phone,Address,CovidStatus) values(%s,%s,%s,%s)",
                    (
                        value['name'], value['phone'], value["address"],
                        [key for key in r_keys if value[key]][0]))
                window2.FindElement("UserError").Update('')
                mycon.commit()

            # Inserting personal info. of users into table (User)

            except sqltor.IntegrityError:
                window2.FindElement("UserError").Update(
                    "A user exists with same phone number.")

        # Helps to restrict duplicacy of data

        else:
            mycur.execute(
                "create table User(UserID int Primary key auto_increment,"
                "Name varchar(18) not null,"
                "Phone BIGINT UNIQUE not null,"
                "Address varchar(30) not null,"
                "CovidStatus varchar(8) not null check (CovidStatus in ('+ve','prob+ve','-ve')))")
            r_keys = ["+ve", "-ve"]

            # Creating table (User) with primary key as user ID which will automatically incrementing

            mycur.execute(
                "insert into User(Name,Phone,Address,CovidStatus) values(%s,%s,%s,%s)",
                (
                    value['name'], value['phone'], value["address"],
                    [key for key in r_keys if value[key]][0]))

            # Inserting values into user
            window2.FindElement("UserError").Update('')
            mycon.commit()
    elif event == "Update":
        window2["CreateUser"].Update(visible=False)
        window2["UpdateUser"].Update(visible=True)
        window2["return"].Update(visible=True)

    # Create user is disables and update user is enabled once update button is clicked

    elif event == "return":
        window2["CreateUser"].Update(visible=True)
        window2["UpdateUser"].Update(visible=False)
        window2["return"].Update(visible=False)

    # Create user is enabled and update user is disabled once return button is clicked

    elif event == "update":
        option = value["l3option"]
        userid = value["UQuery"]
        Nvalue = value["NValue"]
        mycur.execute('use covid19;')
        try:
            mycur.execute("update user set %s='%s' where UserID='%s'" % (
            option, Nvalue, userid))
            mycon.commit()
        except sqltor.DatabaseError:
            print('Value is violating a constraint')
    # Updates info of the user according to the new data provided

    elif event == 'search':
        searchby = value['option']
        query = value['squery']
        if query == '':
            mycur.execute(dbuse)
            mycur.execute("select * from user")
        else:
            mycur.execute(dbuse)
            mycur.execute(
                "select * from user where %s='%s'" % (searchby, query))
        dat = mycur.fetchall()
        window2.FindElement('list').Update(dat)

        # Searches user info according to query entered

    elif event == "hospitallist":
        pincode = sg.popup_get_text("Enter Pincode", "COVID 19")
        print(pincode)
        if pincode not in ('',None):
            query = "covid test centres near {}".format(pincode)
            res = [i for i in search(query, tld="co.in", num=3, stop=3, pause=2)]
            webbrowser.open_new_tab(res[0])

        # opens a tab on the internet to show covid testing centers near 
        # the zipcode entered
    elif event=='delete':
        z = sg.popup_ok_cancel('Confirm Delete?')
        if z != 'Cancel':
            print(z,type(z))    
            mycur.execute('delete from user where userid=%s'%value["UQuery"])
        else:print(z,type(z))
        mycon.commit()
    elif event == "graph":
        try:
            mycur.execute("use covid19")
            mycur.execute("select substring(Address,1,1) as Block,count(*) "
                          "from user "
                          "where covidstatus='+ve' "
                          "group by Block "
                          "order by Block;")

            # Counts number of cases per block

            graphdata = mycur.fetchall()
            blocks = []
            cases = []
            for (i, j) in graphdata:
                blocks.append(i)
                cases.append(j)

            line = plt.bar(blocks, cases)
            plt.xlabel('Blocks')
            plt.ylabel("Cases")

            for i in range(len(cases)):
                plt.annotate(str(cases[i]), xy=(blocks[i], cases[i]),
                             ha='center', va='bottom')

            plt.show()

            # plots graph of number of cases on Y axis vs Blocks on X axis

        except sqltor.Error:
            pass
    elif event == "Clear Database":
        mycur.execute('drop database covid19')
        mycon.commit()

    # Clears existing data in database covid19

    elif event == "Delete Saved Password":
        os.remove(filename)

    # Deletes saved passwords

    elif event == "About...":
        string2 = '''
        Welcome to COVID 19 Case Management Application

        This is a RDBMS based system which logs meetings
                    between Users in the RDBMS

        To start,you need to create users in the Create
        Users section.You can add as many users you want
        and search them in the Search Section

        Once a covid +ve person is logged in a meeting with
        a non COVID person,The covid -ve person is marked as
        prob+ve.You can update any info by clicking the
        update button

        You can also view a graph based on the block vs.
             cases by clicking the graph button '''

        sg.popup(string2, title="About...", grab_anywhere=True)
    elif event == "Help":
        layout3 = [[sg.Text("What can I help you with?"),
                    sg.InputOptionMenu(
                        values=["Formats", "Graphs", "Inputting Data"],
                        k="helpoption", )],
                   [sg.Button("Submit", k="help")],
                   [sg.Text(text="", size=(70, 8), k="L@bel")]]
        window3 = sg.Window(title="Help", layout=layout3)
        while True:
            event1, value1 = window3.read()
            if event1 == sg.WINDOW_CLOSED:
                break
            elif event1 == "help":
                if value1["helpoption"] == "Formats":
                    window3.FindElement("L@bel").Update('''\t\tThe date has to be in YYYY-MM-DD format.Eg:2020-09-12
                    The Address should start with Flat no/Plot no. Example:D-128 ''')

                elif value1["helpoption"] == "Graphs":
                    window3.FindElement("L@bel").Update('''\t     The Graph takes data from the Address and no.of cases
                    (Hence the Block should be First Letter in address)
                    It can be edited using the options provided in the matplotlib library''')
                elif value1["helpoption"] == "Inputting Data":
                    window3.FindElement("L@bel").Update('''\t     The code handles duplicate data for you
                    so no need to worry about that.
                    For deleting user, enter a userid in the field and click delete.
                    You need to enter data manually for each entry. There is not automation available.
                    The data should follow the formats specified and remember to wait after clicking \t\tsubmit''')
        # helps user to use the application smoothly
        window3.close()
window2.close()