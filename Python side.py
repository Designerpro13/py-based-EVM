import time
import os
import csv
file_path='G:\\1Platinum\\autobot'
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
    u_s=str(user)
    if user in auth_ppl:
        pswd=int(input('Enter pass: '))
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
def login(user):
    i=3
    while i>0:
        access(user)
        if aquaint==False:
            print('Try again')
            access(user)
        else:
            break
            return True
    else:
        print('Unable to log you in! Sorry :-(')
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
    
def new_poll2(): #CSV version
    global con_list
    global log_time
    global title
    global list0
    global file_name
    print('You are about to create a new poll')
    time.sleep(0.5)
    log_time = time.ctime() 
    title=input('Enter poll title: ')
    file_name=title+'.csv'
    ask_range=int(input('Enter numbers of posts: '))
    con_header=[]
    cl=open(file_name,'a+',newline='')
    write=csv.writer(cl,delimiter=',')
    for i in range(ask_range):
        print('Enter Post name:',str(i+1)+')',end='')
        con_heads=str(input(''))
        con_header.append(con_heads)        
    else:
        writed=csv.DictWriter(cl,delimiter=',',fieldnames=con_header)
        writed.writeheader()        
        print('You have filled all posts - assign contestants in order :-')
        read=cl.readlines()
        for row in read:
            print(', '.join(row))
    while True:
        time.sleep(0.1)
        enter=eval(input('''Enter Contestant name
                    Within brakets []
                    names in Quotes - \'\'
                    Seperated by comma \',\' 
                    TO EXIT PRESS \'0\':  '''))
        if enter==0:
            break
        else:
            print('Value inserted',enter)
            write.writerow(enter)
    
    cl.close()
    print('\n\nShowing records...')
    with open(file_name,'r+',newline='') as f:
        read=csv.reader(f)
        for q in read:
            print(q)
        
    
'''    
def choose_poll():
    global title
    q=input('Run poll? (Y/N): ')
    if q.lower()=='y':
        print(title) #Name of the SQL tables present in the DB
        with open(file_name,'r+') as lis:
            read=lis.readlines()
            for i in read:
                print(i)
        
        else:
            print('Back to login page')
'''        
def log_set():
    log_session_out=time.asctime(time.localtime())
    set_log(u_n, log_session_in,log_session_out)
    
def read_contents():
    with open(recent_open,'r+') as poll:
        r=csv.reader(poll)
        for i in r:
            print(i)
            
def update_file_name():
    global recent_open
    recent_file.append(file_name)
    recent_open=recent_file.pop()
            
        
        
#_------------------------------------------------------ 

print(''' Welcome to \'Chunav Yantre\'\nThis is a Python - SQL based voting programe.''')
print('You can start working after your authentication')
auth_ppl={'admin':110,'panda':141,'pup':111}
recent_file=[]
title=''
#________________Menu access for user_____________
print('You are requesting to access the ADMIN previdgles\nKindly authorize yourself')
u_n=str(input('Enter Us.name: '))
aquaint=login(u_n)
aquaint
cur_user=u_n.capitalize()
    
if aquaint==True:
#Create a empty file to store and fetch data
    try:
        os.mkdir(file_path)
        os.chdir(file_path)
    except FileExistsError:
        os.chdir(file_path)
    log_session_in=time.asctime(time.localtime())
    print(cur_user,'What would you like to do today? ')
    b='1.Create new poll\n3.View results\n4.View log records\nPress any other key to log off '
    for i in b:
        print(i,end='')
        time.sleep(0.02)
    act=input('Your Quiry: ')
    if act=='1':
        new_poll2()
        update_file_name()    
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
