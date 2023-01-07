#!/usr/bin/python3
import mysql.connector
import getpass
import csv
from csv import reader
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table   
from rich.text import Text
from rich import print
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import track
from rich.progress import Progress
from configparser import ConfigParser



def print_logo():

    console = Console()
    console.set_window_title("DBReader - mysql-client tool")
    console.clear()
    WELCOME = """
# **Welcome to DBReader**
## *Created by M.Witczak*
### 2022
    """

    logo = """

██████╗░██████╗░██████╗░███████╗░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██████╦╝██████╔╝█████╗░░███████║██║░░██║█████╗░░██████╔╝
██║░░██║██╔══██╗██╔══██╗██╔══╝░░██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝██████╦╝██║░░██║███████╗██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """
    w1 = Markdown(WELCOME)

    console.print(w1, style="white", justify="center")
    console.print(logo, style = "bright_cyan", justify="center")
    user_input()





def user_input():
    console = Console()
    
    usr_input = console.input('[bold green]Username: [/]')
    password_input = getpass.getpass('Password: ')
    
    database_input = console.input('[bold yellow]Database name: [/]')
    #Read config file
    config_obj = ConfigParser()
    config_obj.read("dbreader_config.ini")
    user_info = config_obj["USERINFO"]
    dbserver = user_info["host"]
    dbpersona_data = user_info["data_path"]
    try:
        cnx = mysql.connector.connect(user=usr_input, password=password_input,
                                host=dbserver,
                                database=database_input)
    

        with open(dbpersona_data, 'r') as f:
            reader = csv.reader(f)
            lines = sum(1 for line in f)
        console.clear()
        sublogo = """

    █▀▄ █▄▄ █▀█ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█
    █▄▀ █▄█ █▀▄ ██▄ █▀█ █▄▀ ██▄ █▀▄
    """
        console.print(sublogo, style = "bright_cyan", justify="center")
        
        
        
        run(cnx, lines)
    except mysql.connector.Error as err:
        print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
###### Menu
def print_menu():
    print(Panel.fit("""
[white]1.[/white] Create table.
[white]2.[/white] Select all records from selected table.
[white]3.[/white] Select specific records by 'ID' or 'Album'.
[white]4.[/white] Insert DBPersona records.
[white]5.[/white] Delete record.
[white]6.[/white] Drop table.
[white]7.[/white] Truncate table.
[white]8.[/white] Reports.

[red3]Q.[/red3] Quit
""", title="Menu", border_style="bright_cyan", style="bright_cyan"))

def sub_menu():
    print("""
------------------------------
[red3]Q.[/red3] Quit
[yellow1]M.[/yellow1] Main menu
""")

##### Menu choice

def run(cnx, lines):
    print_menu()
    while(True):
        option = ''
        try:
            option = input('Enter your choice: ')
        except:
            print('[red3]Wrong input. Please try again.[/red3]')
        if option == '1':
            print('Create table section')
            create_table(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '2':
            print('Select all section')
            select_all_records(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '3':
            print('Select by id or album section')
            select_by_id_album(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '4':
            print()
            insert_records(cnx, lines)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '5':
            delete_record_by_id(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '6':
            print('Drop table section')
            drop_table(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '7':
            #print('Truncate section')
            truncate_table(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == '8':
            print('Reports section')
            #reports(cnx)
            sub_menu()
            submenu_choice_loop(cnx, lines)
        elif option == 'Q' or option == 'q':
            print("[yellow1 bold]:high_voltage: Bye bye [yellow1 bold]:high_voltage:")
            #reports(cnx)
            exit()
        else:
            print('[yellow1 bold] [blink] Invalid input. Try again![/blink][/yellow1 bold]')
            run(cnx, lines)

def submenu_choice_loop(cnx, lines):                   
        optionS = ''
        while(True):
            try:
                optionS = str(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter Q or M...')
            if optionS == "Q" or optionS == "q":
                print("[yellow1 bold]:high_voltage:[/yellow1 bold] Bye! [yellow1 bold]:high_voltage:")
                cnx.close()
                exit()
            elif optionS == "M" or optionS == "m":
                run(cnx, lines)
            else:
                print('Wrong input. Please enter Q or M...')
####### Show tables:
#cursor2 = cnx.cursor()
#cursor2.execute("Show tables")
#for x in cursor2:
#  print(x) 
#cursor2.close()

def create_table(cnx):
####TO-DO v2 - how many columns, type of data, sql 
    console = Console()
    cursor1 = cnx.cursor()
    try:
        cursor1.execute("CREATE TABLE students (std_id INT AUTO_INCREMENT PRIMARY KEY, imie varchar(25), nazwisko varchar(35), data_urodz date, pesel char(11), email varchar(50), album int(50), wydzial varchar(50))")
    except mysql.connector.Error as err:
        print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
    cursor1.close()
    console.print("[green]Table[/green] [italic] students [/italic][green] has been successfully created![/green]")



####### Insert dbpersona data:
def insert_records(cnx, lines):
    cursor3 = cnx.cursor(buffered=True)
    table_input = input('Please enter table name: ')
    #Read config file
    config_obj = ConfigParser()
    config_obj.read("dbreader_config.ini")
    user_info = config_obj["USERINFO"]
    dbpersona_data = user_info["data_path"]



    with open(dbpersona_data, 'r') as f:
        reader = csv.reader(f)
        count_records = 0
        
        
        
           
        with Progress() as progress:
           
            task1 = progress.add_task("[red]Inserting records", total=lines)
    
            for row in reader:
                r_imie = row[0]
                r_nazwisko = row[1]
                try:
                    raw_date = datetime.strptime(row[2], '%Y-%m-%d')
                    r_data= raw_date.strftime('%Y-%m-%d')
                except ValueError:
                    print('Bad data : ' + str(row))
                r_pesel = row[3]
                r_album = row[5]
                r_email = row[4]
                r_wydzial = row[6]
                

                sql_insert = 'INSERT into '+ table_input + ' (imie, nazwisko,data_urodz, pesel, album,email, wydzial) VALUES (%s, %s, %s,%s, %s, %s,%s)'
                val = (r_imie,r_nazwisko,r_data,r_pesel,r_album,r_email,r_wydzial)
                #print("Record inserted...")
                
                try:
                    cursor3.execute(sql_insert, val)
                    progress.update(task1, advance=1)
                    count_records = count_records + 1
                except mysql.connector.Error as err:
                    print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
                    progress.update(task1, advance=0)
                    break
                
            progress.update(task1, description='[green]Inserting Completed!')

            # cursor3.executemany(sql_insert, data)
        
        
    cnx.commit()
    cursor3.close()
    print(str(count_records) +" records successfully inserted.")

def select_all_records(cnx):
####### Select from table:
    console = Console()
    tableinput = console.input("Please enter table name: ")
    cursor4 = cnx.cursor(buffered=True)
    cursor4.execute("SELECT * from " + tableinput)
    cursor4.close()
    results = cursor4.fetchall()
    
    tab1 = Table(title="ALL records from '" + tableinput + "'", style='bright_cyan')

    tab1.add_column("ID", justify="left")
    tab1.add_column("Imie", justify="left")
    tab1.add_column("Nazwisko", justify="left")
    tab1.add_column("Data urodzin", justify="left")
    tab1.add_column("PESEL", justify="left")
    tab1.add_column("E-mail", justify="left")
    tab1.add_column("Nr albumu", justify="left")
    tab1.add_column("Wydzial", justify="left")

    

    for x in results:
            std_id = x[0]
            imie = x[1]
            nazwisko = x[2]
            data_urodz = x[3]
            pesel = x[4]
            email = x[6]
            album = x[5]
            wydzial = x[7]
#imie, nazwisko,data_urodz, pesel, album,email, wydzial
            tab1.add_row("[brightcyan]"+str(std_id),imie,nazwisko,str(data_urodz),pesel,str(album),str(email),wydzial)
    
    
    
    print(tab1)
    SUMMARY = """
# DBreader 2022
    """
    w1 = Markdown(SUMMARY)
    console.print(w1, style="green", justify="center")
    del results

def select_by_id_album(cnx):
####### Select from table:
    console = Console()
    tableinput = console.input("Please enter table name: ")
    idinput = console.input("Please enter ID value: ")
    albuminput = console.input("Please enter Album value ([italic]optional[/italic]): ")
    cursor5 = cnx.cursor(buffered=True)
    try:
        if idinput.isnumeric():
            try:
                cursor5.execute("SELECT * from "+ tableinput + " where std_id="+str(idinput))
            except:
                print('\n[blink]Wrong input. Please try again.[/blink]')
        elif (idinput=="") & albuminput.isnumeric():
            try:
                cursor5.execute("SELECT * from "+ tableinput + " where album="+str(albuminput))       
            except:
                print('\n[blink]Wrong input. Please try again.[/blink]')
        elif idinput.isnumeric() & (albuminput == ''):
            try:
                cursor5.execute("SELECT * from "+ tableinput + " where std_id="+str(idinput))       
            except:
                print('\n[blink]Wrong input. Please try again.[/blink]')
        else:
            try:
                print('\n[blink]Wrong input. Please try again.[/blink]')
            except mysql.connector.Error as err:
                print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
    
    
        
        results = cursor5.fetchall()
        cursor5.close()
    
        tab2 = Table(title="Selected records from '" + tableinput + "'", style='bright_cyan')

        tab2.add_column("ID", justify="left")
        tab2.add_column("Imie", justify="left")
        tab2.add_column("Nazwisko", justify="left")
        tab2.add_column("Data urodzin", justify="left")
        tab2.add_column("PESEL", justify="left")
        tab2.add_column("E-mail", justify="left")
        tab2.add_column("Nr albumu", justify="left")
        tab2.add_column("Wydzial", justify="left")

        

        for x in results:
                std_id = x[0]
                imie = x[1]
                nazwisko = x[2]
                data_urodz = x[3]
                pesel = x[4]
                email = x[6]
                album = x[5]
                wydzial = x[7]
    #imie, nazwisko,data_urodz, pesel, album,email, wydzial
                tab2.add_row("[brightcyan]"+str(std_id),imie,nazwisko,str(data_urodz),pesel,str(album),str(email),wydzial)
        
        
        
        print(tab2)
        SUMMARY = """
# DBreader 2022
    """
        w1 = Markdown(SUMMARY)
        console.print(w1, style="green", justify="center")
        
     
    except mysql.connector.Error as err:
        print("[yellow3]Something went wrong[/yellow3]: {}".format(err))

####### Delete record:
def delete_record_by_id(cnx):
    table_input = input('Please enter table name: ')
    id_input = input('Please enter ID: ')
    cursor9 = cnx.cursor()
    console = Console()
    while(True):
            try:
                optionS = console.input('[red]Are you sure? [y/n]: [/red]')
            except:
                print('Wrong input. Please enter Y/y or N/n...')
            if optionS == "Y" or optionS == "y":
                try:
                    #cursor9.execute('DELETE FROM'+table_input+'WHERE ID='+str(id_input))
                    print('DELETE FROM '+table_input+' WHERE ID='+str(id_input))
                    break
                   
                except mysql.connector.Error as err:
                    print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
                    cursor9.close()
            elif optionS == "N" or optionS == "n":
                
                break
            else:
                print('Wrong input. Please enter Y or N...')
                cursor9.close()

    cursor9.close()

####### Drop table:
def drop_table(cnx):
    table_input = input('Please enter table name: ')
    cursor8 = cnx.cursor()
    console = Console()
    while(True):
            try:
                optionS = console.input('[red]Are you sure? [y/n]: [/red]')
            except:
                print('Wrong input. Please enter Y/y or N/n...')
            if optionS == "Y" or optionS == "y":
                try:
                    cursor8.execute('DROP TABLE '+table_input)
                    print("Drop Completed")
                    break
                   
                except mysql.connector.Error as err:
                    print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
                    cursor8.close()
            elif optionS == "N" or optionS == "n":
                
                break
            else:
                print('Wrong input. Please enter Y or N...')
                cursor8.close()

    cursor8.close()


####### Truncate table:
def truncate_table(cnx):
    table_input = input('Please enter table name: ')
    cursor7 = cnx.cursor()
    console = Console()
    while(True):
            try:
                optionS = console.input('[red]Are you sure? [y/n]: [/red]')
            except:
                print('Wrong input. Please enter Y/y or N/n...')
            if optionS == "Y" or optionS == "y":
                try:
                    cursor7.execute('TRUNCATE TABLE '+table_input)
                    print("Truncate Completed")
                    break
                   
                except mysql.connector.Error as err:
                    print("[yellow3]Something went wrong[/yellow3]: {}".format(err))
                    cursor7.close()
            elif optionS == "N" or optionS == "n":
                
                break
            else:
                print('Wrong input. Please enter Y or N...')
                cursor7.close()

    cursor7.close()

    
   






   

if __name__ == "__main__":
    print_logo()
