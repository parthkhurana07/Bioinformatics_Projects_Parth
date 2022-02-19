import pandas as pd
import matplotlib.pyplot as plt
print("project is based on Webseries")
print("------------------------------------")
df=pd.read_csv('Webseries.csv')
print("------------------------------------")
print("------------------------------------")
while(True):
    print(" Main Menu")
    print("1. Show Data")
    print("2. Inforamtion about the Webseries")
    print("3. Attributes of Webseries DataFrame")
    print("4. Display Records")
    print("5. Insertion/Deletion/Updation of Records")
    print("6. Insertion/Deletion of columns")
    print("7. Garaphical representation")
    print("8. Exit")
    print("------------------------------------")
    ch=int(input("Enter your Choice"))
    if ch==1:
          print(df)
    elif ch==2:
        print("   this is a .........")
        #print(df.info())
    elif ch==3:
        print("------------------------------------")
        #while(True):
    print("1. Display Rows of the Webseries")
    print("2. Display columns of the Webseries")
    print("3. Display Both Rows and Columns of the Webseries")
    print("4. Display datatype of data in the Webseries")
    print("5. Display the size of the Webseries")
    print("6. Display the shape of the Webseries")
    print("7. Display Axes of the Webseries")
    print("8. Transpose Rows and Columns of the Webseries")
    print("9. Check wether the Webseries is empty or not")
    print("10. Exit")
              ch3=int(input("Enter Choice"))
              if ch3==1:
                    print(df.index)
              elif ch3==2:
                    print(df.columns)
              elif ch3==3:
                    print(df.axes)
              elif ch3==4:
                    print(df.dtypes)
              elif ch3==5:
                    print(df.size)
              elif ch3==6:
                    print(df.shape)
              elif ch3==7:
                    print(df.ndim)
              elif ch3==8:
                    print(df.T)
              elif ch3==9:
                    print(df.empty)
              #elif ch3==10:
                #    break
    elif ch==4:    
        print("------------------------------------")
       # while(True):
              print("Display Records Menu")
              print("1. Top 5 Records")
              print("2. Bottom 5 Records")
              print("3. Specific number of records from the top")
              print("4. Specific number of records from the bottom")
              print("5. Details of a specific Webseries")
              print("6. Exit")
              ch4=int(input("Enter choice"))
              if ch4==1:
                    print(df.head())
              elif ch4==2:
                    print(df.tail())
              elif ch4==3:
                    n=int(input("Enter how many records you want to display from the top"))
                    print(df.head(n))
              elif ch4==4:
                    n=int(input("Enter how many records you want to display from the bottom"))
                    print(df.tail(n))
              elif ch4==5:
                    e=int(input("Enter the Webseries_id to see the details"))
                    print(df.loc[e])
             # elif ch4==6:
                  #  break
    elif ch==5:
        print("------------------------------------")
       # while(True):
              print("1. Add a row")
              print("2. Modify a row")
              print("3. Rename a row")
              print("4. Delete a row")
              print("5. Exit")
              ch5=int(input("Enter Choice"))
              if ch5==1:
                    p=input("Enter the name or number of row you wanna add")
                    o=int(input("Enter the values you wanna give to that row"))
                    df.at[p,:]=o
                    print(df)
              elif ch5==2:
                    i=int(input("Enter the number of a existing row which you wanna modify"))
                    j=input("Enter the values you wanna change")
                    df.loc[i,:]=[j]
                    print(df)
              elif ch5==3:
                    u=int(input("Enter the number of row you wanna rename"))
                    h=input("Enter the new name of row")
                    print(df.rename(index={u:h}))
              elif ch5==4:
                    g=int(input("Enter the number of row you wanna delete"))
                    print(df.drop(g))
            #  elif ch5==5:
                #    break
    elif ch==6:
        print("--------------------------------------")
       # while(True):
              print("1. Add a Column")
              print("2. Modify a column")
              print("3. Rename a column")
              print("4. Delete a column")
              print("5. Exit")
              ch6=int(input("Enter choice"))
              if ch6==1:
                    n=input("Enter the Name of column you wanna add")
                    g=int(input("Enter the values you wanna put in thr new column"))
                    df.at[:,n]=[g]
                    print(df)
              elif ch6==2:
                    y=input("Enter the name of existing column ehich you wanna modify")
                    q=input("Enter the value you wanna modify in existing  modified column")
                    df.loc[:,y]=[q]
                    print(df)
              elif ch6==3:
                    k=input("Enter the name of column you wanna rename")
                    l=input("Enter the new name of column")  
                    print(df.rename(columns={k:l}))
              elif ch6==4:
                    h=input("Enter the Name of column you wanna delete") 
                    del df[h]
                    print(df)
             # elif ch6==5:
                 #   break  
    elif ch==7:
        print("--------------------------------------")
       # while(True):
              print("1. Line Chart")
              print("2. Bar graph")
              print("3. histogram")
              print("4. Exit")
              ch7=int(input("Enter Choice"))
              if ch7==1:
                    df.plot(x ='No_of_Episodes', y='No_of_Seasons')
                    plt.show()
              elif ch7==2:
                    df.plot(x ='No_of_Episodes', y='No_of_Seasons',kind='bar')
                    plt.show() 
              elif ch7==3:
                    df.hist(bins=30)
                    plt.show()
              #elif ch7==4:
                 #   break
                    
    elif ch==8:
        print("--------------------------------------")
        break

        

