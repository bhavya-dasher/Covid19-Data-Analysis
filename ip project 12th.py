#Date- 13 Feb. 2021
#Covid-19 info about cases and deaths of the world a/c to WHO by graphical method.
#Program consists of all types of functions including matplotlib,etc.

#Source code:-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
pd.set_option('max_columns',None)

global df
df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
df=pd.read_excel(open("C:\\Users\\DELL\\Downloads\\Top11CountriesCovid_19data.xls",'rb'))

#--------------------------
#Function to Plot graphs
#--------------------------

def visuals():
    ch='y'
    while (ch=='y' or ch=='Y'):
        print()
        print("*******************************************\n")
        print(" Data Visualization Menu- Top 11 Countries ")
        print("===========================================\n")
        print("1- Line Chart- Total(cases vs deaths)\n")
        print("2- Pie Chart- Most Cases of country\n")
        print("3- Bar Chart- Total cases of WHO region\n")
        print("4- Pie Chart- Most Deaths of country\n")
        print("5- Bar Chart- Total deaths of WHO region\n")
        print("6- Histogram- Total Cases and Deaths per 100000 population\n")
        print("7- Exit\n")
        print("===========================================")
        opt1=input("Enter your choice:-")
        if opt1=='1':
            line_chart()
        elif opt1=='2':
            pie_chart_1()
        elif opt1=='3':
            bar1()
        elif opt1=='4':
            pie_chart_2()
        elif opt1=='5':
            bar2()
        elif opt1=='6':
            histogram()
        elif opt1=='7':
            chance=input("Do you really want to exit and go back to main menu?(y/n)")
            if chance=='y' or chance=='Y':
                print("Exiting.........")
                break
        else:
            print("\nInvalid input. Try again")
            continue
    else:
        ch=input("Do you want to continue(y/n)")

#--------------------------------------------------------------
#Function to Plot Line Chart for Total cases vs total deaths
#--------------------------------------------------------------

def line_chart():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    f = plt.figure() 
    f.set_figwidth(8) 
    f.set_figheight(5)
    x1=df['Name'].head(11)
    x=df['Cases - cumulative total'].head(11)
    y=df['Deaths - cumulative total'].head(11)
    plt.plot(x1,x,label="Total Cases",linewidth=3,marker='o',markeredgecolor='r',markersize=2,linestyle="solid")
    plt.plot(x1,y,label="Total Deaths",linewidth=2,marker='o',markeredgecolor='r',markersize=2,linestyle="dashed")
    plt.title("Covid-19 Analysis\nTop 11 countries\nDate=13th Feb. 2021",color='red',fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()

#-----------------------------
#Function to Plot Pie Chart 
#-----------------------------

def pie_chart_1():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    f = plt.figure() 
    f.set_figwidth(8) 
    f.set_figheight(4)
    a=df['Name'].head(11)
    b=df['Cases - cumulative total'].head(11)
    plt.pie(b,labels=a,autopct="%1.1f%%",explode=[0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
    plt.title('Most cases in Top11 countries',fontsize=20,color='red')
    plt.show()

#-----------------------------
#Function to Plot Bar Chart 
#-----------------------------

def bar1():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    f = plt.figure() 
    f.set_figwidth(9) 
    f.set_figheight(5)
    x=df['WHO Region'].head(15)
    y=df['Cases - cumulative total'].head(15)
    plt.bar(x,y,color='r',width=0.4)
    plt.xlabel('WHO region',fontsize=15)
    plt.ylabel('Total Cases in crore',fontsize=15)
    plt.title('Total cases in 100 countries under WHO region',fontsize=20,color='red')
    plt.show()

#*****************************

def pie_chart_2():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    m=df['Name'].head(11)
    m1=df['Deaths - cumulative total'].head(11)
    plt.pie(m1,labels=m,autopct="%1.1f%%",explode=[0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
    plt.title('Most deaths in Top11 countries',fontsize=20,color='red')
    plt.show()

#*****************************

def bar2():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    f = plt.figure()
    f.set_figwidth(9) 
    f.set_figheight(5)
    k=df['WHO Region'].head(15)
    v=df['Deaths - cumulative total'].head(15)
    plt.bar(k,v,color='r',width=0.4)
    plt.xlabel('WHO region',fontsize=15)
    plt.ylabel('Total Deaths in lacs',fontsize=15)
    plt.title('Total deaths in 100 countries under WHO region',fontsize=20,color='red')
    plt.show()


#-----------------------------
#Function for Histogram Plot 
#-----------------------------

def histogram():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
    b=df['Cases - cumulative total per 100000 population'].head(11)
    g=df['Deaths - cumulative total per 100000 population'].head(11)
    bg=np.array(b,g)
    plt.hist(bg,bins=7,orientation='vertical',edgecolor="black",histtype="barstacked",cumulative=True)
    plt.xlabel("Cases per 100000 population",fontsize=12,color='b')
    plt.ylabel("Deaths per 100000 population",fontsize=12,color='m')
    plt.title('Total cases and deaths per 100000 population',fontsize=15,color='red')
    #plt.grid()
    plt.show()

#-------------------------------------------
#Function to analyse data from a dataframe
#-------------------------------------------
    
def analysis():
    while True:
        print()
        print("*************************")
        print("   Data Frame Analysis   ")
        print("=========================")
        print("1. Top records")
        print("2. Bottom records")
        print("3. To print particular column")
        print("4. To display complete statitics of the dataframe")
        print("5. To display complte information about dataframe")
        print("6. To display the unique values of the columns")
        print("7. To applying aggregate function")
        print("8. Exit")
        print("=============================")
        df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
        ch_an=int(input("Enter your choice:-"))
        if ch_an==1:
            print(df.columns)
            n=int(input("Enter the number of records to be displayed:-"))
            print("Top ",n," records from the dataframe")
            #print(df.sort_values(by=['Cases - cumulative total'],ascending=[False],inplace=True))
            print(df.head(n))
        elif ch_an==2:
            print(df.columns)
            n=int(input("Enter the number of records to be displayed:-"))
            print("Bottom ",n," records from the dataframe")
            print(df.tail(n))
        elif ch_an==3:
            print("Name of the columns")
            print(df.columns)
            col=input("Enter the column name to be displayed:-")
            print(df[[col]])
        elif ch_an==4:
            print("Complete Statistics")
            print(df.describe())
        elif ch_an==5:
            print("Information about dataframe")
            print(df.info())
        elif ch_an==6:
            print("Dispaying unique values of any columns")
            print("Name of the columns")
            print(df.columns)
            co=input("Enter the column name:-")
            print("Distinct values of column ",co," are: ")
            print(*df[co].unique(),sep='\n') #print(df[co].unique(),sep='\n')
        elif ch_an==7:
            print()
            print("Applying aggregate functions")
            print("Name of the columns")
            print(df.columns)
            co=eval(input("Enter the column names as list in square bracket:-"))
            print('Print the maximum values of the ',co,' columns')
            print(df[co].max())
        else:
            break

#----------------------------------
#Function to read CSV/Excel file
#----------------------------------

def read_csv_excel():
    while True:
        print("1. Read CSV file to create and display DataFrame")
        print("2. Read Excel file and display DataFrame")
        print("3. Press 3 to go back")
        choice=int(input("Enter your choice:-"))
        if choice==1:
            df=pd.read_csv("C:\\Users\\DELL\\Downloads\\WHO1.csv")
            print(df)
            print("File retrieved Successfully!!")
        elif choice==2:
            df=pd.read_excel("C:\\Users\\DELL\\Downloads\\Top11CountriesCovid_19data.xls")
            print(df)
            print("File retrieved Successfully!!") 
        elif choice==3:
            break


#---------------------------------------------------
#Function to manipulate the data from a DataFrame
#---------------------------------------------------

def manipulation():
    df=pd.read_csv("C:\\Users\\DELL\\Downloads\\Top11CountriesCovid_19data.csv")
    while True:
        print()
        print("Manipulation Menu")
        print("-----------------")
        print("1. Add a new column")
        print("2. Add a new record")
        print("3. Delete a column")
        print("4. Delete a record")
        print("5. Update Records")
        print("6. Update Column Name")
        print("7. Exit")
        print()
        chc=int(input("Enter your choice:-"))
        if chc==1:
            print(df.columns)
            u=input("Name of new column you want to add:-")
            l=list()
            for i in range(len(df)):
                k=input("Enter values:-")
                l.append(k)
            df[u]=l
            print(df)
        elif chc==2:
            print(df)
            w=list(df.columns)
            w1=df.count(1)[1]
            p=int(input("Enter the new record index position:-"))
            l=[]
            print(df.columns)
            for i in range(len(w)):
                f=input("Enter the values of new records:-")
                l.append(f)
            df.at[p,:]=l
            print("New record inserted at new index position",p)
            print(df)
        elif chc==3:
            print("Name of columns")
            print(df.columns)
            t=input("Name of the column you want to delete:-")
            print()
            del df[t]
            print("column",t,"deleted successfully")
            print(df)
        elif chc==4:
            print(df)
            s=int(input("Index position of record you want to delete:-"))
            print()
            q=df.drop([s],axis=0)
            print("record",s,"deleted successfully")
            print(q)
        elif chc==5:
            print("Name of columns")
            print(df.columns)
            w=int(input("How many records do you want to update:"))
            n=input("Are you want to update multiple values of a single column (y/n):")
            print()
            if  n=='y' or n=='Y':
                u=input("Enter column name you want to update:")
            else:
                pass
            for i in range(w):
                if n=='y' or n=='Y':
                    r=int(input("Enter the index value:"))
                    print("Enter new value in column",u,"at index position",r)
                    t=input("-:")
                    print()
                    df.loc[r,u]=t
                    print(df)
                    print()
                elif n=='n' or n=='N':
                    u=input("Enter column name of the record you want to update:")
                    r=int(input("Enter the index value:"))
                    print("Enter new value in column",u,"at index position",r)
                    t=input("-:")
                    df.loc[r,u]=t
                    print(df)
        elif chc==6:
            print(df.columns)
            m=input("Enter column name you want to update:-")
            n=input("Enter new column name:-")
            df.rename(columns={m:n},inplace=True)
            print(df)
        elif chc==7:
            print("Exiting.....")
            break


#-----------------------
#Function to main menu
#-----------------------

def Mainmenu():
    ans='y'
    while ans=='y' or ans=='Y':
        opt=""
        print()
        print("                                   Covid-19 Pandemic Analysis System  ")
        print("                                 -------------------------------------")
        print("1- Data Visualization\n")
        print("2- Analysis\n")
        print("3- Read csv/excel file\n")
        print("4- Manipulation\n")
        print("5- Exit")
        print("=====================================")
        opt=input("Enter your choice:-")
        if opt=='1':
            visuals()
        elif opt=='2':
            analysis()
        elif opt=='3':
            read_csv_excel()
        elif opt=='4':
            manipulation()
        elif opt=='5':
            my_chance=input("Do you really want to exit?(y/n)")
            if my_chance=='y' or my_chance=='Y':
                print("Thank you. Exiting now.....")
                sys.exit()
        else:
            print("\nInvalid choice. Try again")
            continue
    else:
        ans=input("Do you want to continue(y/n)")
Mainmenu()




  


            
        
            
