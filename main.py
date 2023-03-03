import pandas as pd


#ingesting file to be read. This needs to be a .csv file
testFile = pd.read_csv('thisnewcopy.csv')


#getting only the columns that we want including check number, total payments, date of payment, and date of entry

fourColumns = testFile[["Check Number", "Total Payments", "Date of Deposit", "Date of Entry", "Visit - Primary Carrier"]]


#sanity check
#print(fourColumns.shape)


# gettingRifOfNoCheck = fourColumns["Check Number"].notna()
#
#
# print(gettingRifOfNoCheck.describe())


sortedList = fourColumns.sort_values(by="Check Number")

# print(sortedList)

#changing to a dictitoary

toDict = sortedList.to_dict()

#
# print(toDict['Check Number'])


testing = fourColumns[fourColumns["Check Number"] == '0000205937']

# print(testing)


#print a list of checking numbers

checking_first = fourColumns["Check Number"]

checking_list = checking_first.to_list()



for i in range (1,len(toDict['Check Number'])-1):
    if len(checking_list[i]) > 1 :
        total = 0
        new_list = checking_list[i]
        first = fourColumns[fourColumns["Check Number"] == str(new_list)]
        total += fourColumns["Total Payments"]
        new_dict = first.sum()
        print(new_dict)
