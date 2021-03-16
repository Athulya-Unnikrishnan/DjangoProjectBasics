import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print('\t\t\t\t                |                           | ')
print('\t\t\t\t                | IPL2020 PLAYERS DATASET   | ')
print('\t\t\t\t                |___________________________| ')
print('\t\t\t\t                                              ')
print('  ')
def Read_csv():
      print("Reaing Data from csv file")
      print("-------------------------")
      #df=pd.read_csv("C:\\Users\\admin\\Desktop\\ip_ipl.csv")
      df=pd.read_csv(r"C:\Users\\athul\\Downloads\\ip_ipl.csv")
      print(df)
def no_index():
      print("Reading complete file without index")
      print("-----------------------------------")
      #df=pd.read_csv("C:\\Users\\admin\\Desktop\\ip_ipl.csv",index_col=0)
      df=pd.read_csv(r"C:\Users\\athul\\Downloads\\ip_ipl.csv",index_col=0)
      print(df)
def line_chart():
      print("LINE CHART")
      print("----------")
      #df=pd.read_csv("C:\\Users\\admin\\Desktop\\ip_ipl.csv")
      df=pd.read_csv(r"C:\Users\\athul\\Downloads\\ip_ipl.csv")
      x=df["Name_Of_Player"]
      y=df["Matches"]
      plt.plot(x,y,color="r",linestyle="--")
      plt.xlabel("Name_Of_Player")
      plt.ylabel("Matches")
      plt.title("IPL2020 PLAYERS DATASET",color="r")
      plt.show()
      print(df)
def bar_plot():
      #df=pd.read_csv("C:\\Users\\admin\\Desktop\\ip_ipl.csv")
      df=pd.read_csv(r"C:\Users\athul\Downloads\\ip_ipl.csv")
      print("BAR PLOT")
      print("--------")
      plt.bar(df["Name_Of_Player"],df["Matches"],color="r")
      plt.xlabel("Name_Of_Player")
      plt.ylabel("Matches")
      plt.title("IPL2020 PLAYERS DATASET",color="r")
      plt.show()
def hist():
      df=pd.read_csv("C:\\Users\\admin\\Desktop\\ip_ipl.csv")
      #df=pd.read_csv(r"C:\Users\athul\Downloads\\ip_ipl.csv")
      print("HISTOGRAM")
      print("---------")
      df['Runs_Scored'], df['Matches'].plot(kind='hist')
      plt.xlabel("Name Of Player")
      plt.ylabel("Matches")
      plt.title("IPL2020 PLAYERS DATASET",color="b")
      plt.show()
while True:
    print('.....................................')
    print("Read Data from file in different way")
    print("1.Read complete csv file")
    print("2.Reading complete file without index")
    print("DATA VISUALISATION")
    print("3. Line chart")
    print("4. bar plot")
    print("5. histogram")
    print("6. scatter chart")
    print("......................................")
    print("7. sorting the data as per your choice")
    print("......................................")
    x=int(input("enter the choice number"))
    if x==1:
        Read_csv()
        x=int(input("enter the choice number"))
    elif x==2:
        no_index()
        x=int(input("enter the choice number"))
    elif x==3:
        line_chart()
        x=int(input("enter the choice number"))
    elif x==4:
        bar_plot()
        x=int(input("enter the choice number"))
    elif x==5:
        hist()
        x=int(input("Enter the choice number"))
