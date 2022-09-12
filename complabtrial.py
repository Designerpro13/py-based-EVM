import time
import os
import csv
import mysql.connector as mc
file_path='C:\\Users\\Administrator\Desktop\Desktop'
#_------------------------------------------------------
def donothing():
     print()
     pass
def set_log(user, timein, timeout):
    global log_list
    log_list={'user':user,'Time-in':timein,'Time-out':timeout}
    with open(file_path + '\\user_log.txt','a+') as log:
        log.writelines(str(log_list))
        log.writelines('\n')
        
def view_log():
    with open(file_path+'\\user_log.txt','rt') as lg:
        for q in lg:
            print(q,end='\n')
    print('...Current session exculded...')
def access(user):
    global u_s
    u_s='admin'
    if user in auth_ppl:
        pswd=110
        if pswd is auth_ppl[u_s]:
            time.sleep(1)
            print('Access granted. Welcome',user.upper())
            return True
        else:
            print('Access Denied-FALSE PASSWORD')
            return False
    else:
        print('Access denied-FALSE USER')
        return False
def create(user,pswd):
    global new_ppl    
    if user in auth_ppl:
        print('User already exists')
        return None
    else:
        new_ppl[str(user)]:pswd
        print('User added: You can access your account after the Admin authorises you.')
        time.sleep(1.5)
        print('User added: Re-run programme - Exiting console in t-10sec...')
        for i in range(10,0,-1):
            print(i,end=' ')
            time.sleep(1)
        else:
            print('...')
        return False
def new_poll2():#SQL version
    my_config={'host':'localhost','username':'root','password':'1234','database':'ngp','port':'3310'}
    con=mc.connect(**my_config)
    cur=con.cursor()
    print('You are about to create a new poll')
    time.sleep(0.5)
    log_time = time.ctime() 
    title=input('Enter poll title: ')
    ask_range=int(input('Enter numbers of posts: '))
    con_header=[]
    for i in range(ask_range):
        print('Enter Post name:',str(i+1)+')',end='')
        con_heads=str(input(''))
        con_header.append(con_heads)        
    else:       
        print('You have filled all posts - assign contestants in order :-')

    for i in range(ask_range):
        print('For post',i+1)
        qry="create table if not exists {0} (name varchar(24),class varchar(23),image_location varchar(150),votes int default 0)".format(title)
        cur.execute(qry)
        con.commit()
        while True:
            time.sleep(0.1)
            name=input('''Enter contestant name
                        TO EXIT ENTER 0: ''')
            grade=input('Enter contestant grade: ')
            image_address=input('Enter the image address: ')
            qry="insert into table {0} values ({1},{2},{3})".format(title,name,grade,image_address)
            cur.execute(qry)
            con.commit()
            if name==0:
                break
            else:
                print('Values inserted',[name,grade,image_address])

        print('\n\nShowing records for table',con_header[i],'...')
        qry='select * from "{}"'.format(con_header[i])
        cur.execute(qry)
        result=cur.fetchall()
        print('NAME     CLASS      IMAGE ADDRESS    VOTE COUNT')
        for row in result:
            print(row)
                        
def log_set():
    log_session_out=time.asctime(time.localtime())
    set_log(u_n, log_session_in,log_session_out)
    
def read_contents():
    with open(recent_open,'r+') as poll:
        r=csv.reader(poll)
        for i in r:
            print(i)
              
        
#_------------------------------------------------------ 

print(''' Welcome to \'Chunav Yantre\'\nThis is a Python - SQL based voting programe.''')
print('You can start working after your authentication')
auth_ppl={'admin':110,'panda':141,'pup':111}
recent_file=[]
title=''
#________________Menu access for user_____________
print('You are requesting to access the ADMIN previdgles\nKindly authorize yourself')
u_n='admin'
cur_user=u_n.capitalize()
aquaint=access(u_n)
aquaint
if aquaint==True:
#Create a empty file to store and fetch data
    try:
        os.mkdir(file_path)
        os.chdir(file_path)
    except FileExistsError:
        os.chdir(file_path)
    log_session_in=time.asctime(time.localtime())
    print(cur_user,'What would you like to do today? ')
    b='1.Create new poll\n2.View results\n3.View log records\nPress any other key to log off '
    for i in b:
        print(i,end='')
        time.sleep(0.02)
    act=input('Your Quiry: ')
    if act=='1':
        new_poll2()   
        log_set()
    elif act=='2':
        view_log()
        log_set()
    elif act=='3':
        view_log()
        log_set()
    else:
        print('Give me a moment to process')
        time.sleep(1.5)
        print('Logging you off... Bye!')
else:
    log_session_in=0
    log_set()
