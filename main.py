#Initial coding

#print("hello what is your name")
#myName = input()
#print("Really good to see you here, " + myName)
#print("Fun fact, the length of your name is:")
#print(len(myName))
#print("what is your age?")
#myAge = input()
#print("Do you know you will be " + str(int(myAge)+6)+ " in six years time?")
#print("I know, mind blowing!! "+ myName)
#print("OK, enough talking, let's do this")

#====================================================================================================
#I am not merging datasets in my Amazon books project but I would like to include this example below from the first project that I started.
# I had to leave it aside as I hit some roadblocks and couldn't continue.

#df07 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2007.csv")
#print(df07.head(11))
#print(df07.tail(5))
#print(df07.shape)
#print(df07.columns)
#print(df07.dtypes)
#print(df07.loc[1:1000, "Year":"Engine type"])
#print(df7)

#checking columns and items and importing the rest of the datasets

#df08 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2008.csv")
#df09 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2009.csv")
#df010 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2010.csv")
#df011 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2011.csv")
#df012 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2012.csv")
#df013 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2013.csv")
#df014 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2014.csv")
#df015 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2015.csv")
#df016 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2016.csv")
#df017 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2017.csv")
#df018 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2018.csv")
#df019 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2019.csv")

#changing the name of the datasets to avoid confusion and not miss any when merging them.

#df1 = pd.DataFrame(df07, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df2 = pd.DataFrame(df08, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df3 = pd.DataFrame(df09, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df4 = pd.DataFrame(df010, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df5 = pd.DataFrame(df011, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df6 = pd.DataFrame(df012, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df7 = pd.DataFrame(df013, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df8 = pd.DataFrame(df014, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df9 = pd.DataFrame(df015, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df10 = pd.DataFrame(df016, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df11 = pd.DataFrame(df017, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df12 = pd.DataFrame(df018, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
#df13 = pd.DataFrame(df019, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])

# I have concatenated my 13 datasets into one and call it cars.

#cars = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13], ignore_index=True)
#I am ignoring the index to avoid duplicated index numbers carried over from all the different datasets.

#===================================================================================================



#importing packages and continue with Amazon Books project.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Importing database Amazon bestseller books from Kaggle
df = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\Amazonbooks\bestsellers with categories.csv")
#see first five
#print(df.head())
#print(df.dtypes)
#see the number or rows and columns
#print(df.shape)
#print(df.columns)

#checking NaN values
#print(df.isnull().sum())
#I don't have any

##########if I want to fill the NaN values with zero I would use#####
#df.fillna(0)

###########if I was going to drop the rows and columns with a NaN value, I could do this:#######

########to drop the rows
#df_row = df.dropna(axis = 0)
########to drop the columns
#df = df.dropna(axis=1)
#print(df.isnull().sum())

#I could have replaced the NaN values instead of dropping them too
#print(df.isnull().sum())
#df.fillna(value= "", inplace=True)
#print(df.isnull().sum())

#set display max rows and columns
pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df)
#print(df.columns)

#changing User Rating to User_Rating name column name
df.columns = ["Name", "Author", "User_Rating", "Reviews", "Price", "Year", "Genre"]
#print(df.columns)

#print(df.head())

#slicing / indexing
#print(df.loc[[0, 10], :])

#print(df.iloc[0:3, 1:4])
#print(df.loc[[0, 10], :])
#print(df.loc[0, ["Author", "User_Rating", "Year"]])
#print(df.iloc[5, 3])
#print(df.iloc[1, 1])
#print(df.iloc[7, 5])
#print(df[:10])
#print(df.head(20))

#========================================================

#how many times the books at the top ten have been reviewed (x axis)
#how many times the books at the top ten have been rated (x axis)

Top_Ten = df['Name'].value_counts().iloc[:10]

#print(Top_Ten)

#x = Top_Ten
#y1 = df["Reviews"].head(10)
#y2 = df["User_Rating"].head(10)

#fig, (ax1,ax2) = plt.subplots(2,1)

#ax1.plot(x,y1, marker="o", linestyle="--", color="g", label="Reviews")
#ax1.set_title("Reviews per book")
#ax1.set_xlabel("No.of times book reviewed on the Top Ten")
#ax1.set_ylabel("")
#ax1.legend()
#ax1.grid(False)

#ax2.plot(x,y2,marker="*", linestyle="-.", color="y", label="User_Rating")
#ax2.set_title("User_Rating")
#ax2.set_xlabel("No.of times book rated on the Top Ten")
#ax2.set_ylabel("")
#plt.tight_layout()
#ax2.legend()
#plt.grid(False)

#plt.show()

#====================================================================

#plotting top ten sellers using seaborn

Top_Ten = df["Name"].value_counts().iloc[:10]

plt.figure(figsize=(15,8))
sns.barplot(x=Top_Ten.values, y=Top_Ten.index, color="#9acd32", alpha=.9)
plt.title("Top 10 Bestsellers", fontsize=35)
plt.xlabel("Count", fontsize=12)
plt.ylabel("Book", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

#=====================================================================

#x = df["Author"].head(20)
#y1 = df["Price"].head(20)
#sns.lineplot(x=x,y=y1)
#plt.show()
#=======================================================================
#x = df["Author"].head(20)
#y1 = df["Reviews"].head(20)
#sns.lineplot(x=x,y=y1)
#plt.show()


#=========================================================================

#sns.histplot(df["Genre"],bins=12, color="#228b22")
#plt.title("Fiction Vs Non Fiction", fontsize=32)
#plt.show()

#pie plot to show percentage Fiction books Vs Non Fiction books
Genre = df["Genre"].value_counts()
plt.figure(figsize=(15,7))
plt.pie(Genre, colors=["#ff0000","#ffff00"],autopct="%1.1f%%", startangle=90, shadow=False , explode=(0.3,0), labels=Genre.index)
plt.title("Book Genre", fontsize=30)
plt.show()

#============================================================================
#I want to find the most expensive book in the Dataset
#column = df["Price"]
#max_value = column.max()
#print(max_value)
#locating it by index
#column = df["Price"]
#max_index = column.idxmax()
#rint(max_index)
#print(df.iloc[[69]])
# It's Diagnostic and Statistical Manual of Mental Disorders for 105Eur from Year 2013.

#Now that that works, I can find the cheapest book in the Dataset
#column = df["Price"]
#min_value = column.min()
#print(min_value)
#column = df["Price"]
#min_index = column.idxmin()
#print(min_index)
#print(df.iloc[[42]])
# It's Cabin Fever (Diary of a Wimpy Kid, Book 6) for 0Eur from Year 2011. Although this is not 100% correct as there are more books for free than this one

#=========================================================================
#Now I am going to group the data by Authors
#group=df.groupby("Author")
#print(group)
#print(group.sum())
#which Author has the highest number of combined ratings?
#print(group.sum().sort_values("User_Rating").tail())
#It's Jeff Kinney with 57.6

#which Author has the highest number of reviews?
#print(group.sum().sort_values("Reviews").tail())
#It's Suzanne Collins with 51.3

#===========================================================================

#scatter plot to show the relation between price and User Rating
#df = pd.DataFrame(np.random.rand(50, 4), columns=["Reviews", "Price", "Year", "User_Rating"])
#df.plot.scatter(x="Price", y="User_Rating")
#plt.show()
#scatter plot to show the relation between price and Year
#df = pd.DataFrame(np.random.rand(50, 4), columns=["Reviews", "Price", "Year", "User_Rating"])
#df.plot.scatter(x="Price", y="Year")
#plt.show()
#scatter plot to show the relation between price and Reviews
#df = pd.DataFrame(np.random.rand(50, 4), columns=["Reviews", "Price", "Year", "User_Rating"])
#df.plot.scatter(x="Price", y="Reviews")
#plt.show()

#=====================================================================================

#plot showing relation between the Price, reviews and Ratings.
#x = df["Price"].head(20)
#y1 = df["Reviews"].head(20)
#y2 = df["User_Rating"].head(20)


#fig, (ax1,ax2) = plt.subplots(1,2)

#ax1.plot(x,y1, marker="d", linestyle="--", color="c", label="Reviews")
#ax1.set_title("")
#ax1.set_xlabel("Price")
#ax1.set_ylabel("No of Reviews")
#ax1.grid(True)

#ax2.plot(x,y2,marker="^", linestyle="-.", color="g", label="User_Rating")
#ax2.set_title("")
#ax2.set_xlabel("Price")
#ax2.set_ylabel("User_Rating")
#plt.tight_layout()
#plt.grid(True)

#plt.show()
#==================================================================

#I am plotting an histogram showing the frequency of Reviews occurrences.
#sns.histplot(df["Reviews"])
#plt.show()

#reviews = df[["Reviews","Author"]].groupby([df.Author])
#rev_sum = reviews.sum()
#print(rev_sum)

#=======================================================================

