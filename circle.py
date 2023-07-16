import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
mydb = mysql.connector.connect(host='localhost',password='@spiderweb45', user= 'root',database='ss')
mycursor = mydb.cursor()

mycursor.execute("Select * from ss.1000cr_a")
table_1000cr= mycursor.fetchall()
mycursor.execute("Select * from ss.2500cr_a")
table_2500cr= mycursor.fetchall()

# Converting lists to dataframes and assigning column names for easy access
df1 = pd.DataFrame(table_1000cr)
df1.columns=['a','b','c','d','e','f','g']
df2 = pd.DataFrame(table_2500cr)
df2.columns=['a','b','c','d','e','f','g']

# District Function
def District_Table(district_name):
    District = pd.DataFrame(data=0, columns=['Length in kms(1000cr)', 'No. of works(1000cr)',
                                                  'Amount (Rs. In Lakhs)(1000cr)', 'Length in kms(2500cr)',
                                                  'No. of works(2500cr)', 'Amount (Rs. In Lakhs)(2500cr)',
                                                  'Length in kms(total)', 'No. of works(total)',
                                                  'Amount (Rs. In Lakhs)(total)'],
                                 index=['Works Sanctioned', 'Works Completed', 'Works in progress',
                                        'Tenders received and Work about to be started',
                                        'Estimate stage/Tenders no response/Work not yet entrusted'])

    columns = ['Length in kms(1000cr)', 'No. of works(1000cr)', 'Amount (Rs. In Lakhs)(1000cr)',
               'Length in kms(2500cr)', 'No. of works(2500cr)', 'Amount (Rs. In Lakhs)(2500cr)', 'Length in kms(total)',
               'No. of works(total)', 'Amount (Rs. In Lakhs)(total)']
    index = ['Works Sanctioned', 'Works Completed', 'Works in progress',
             'Tenders received and Work about to be started',
             'Estimate stage/Tenders no response/Work not yet entrusted']
    iter = ['work completed','work in progress','tender recieved','estimate']
    i=1
    for x in iter:
        list = []

        # First 3 entries in one row
        Constituency_df = df1[df1['b'] == district_name]

        y = Constituency_df.loc[Constituency_df['g'] == x, 'e'].sum()
        list.append(y)
        y = (Constituency_df.g.values == x).sum()
        list.append(y)
        y = Constituency_df.loc[Constituency_df['g'] == x, 'f'].sum()
        list.append(y)

        # Second 3 entries in one row
        Constituency_df = df2[df2['b'] == district_name]

        y = Constituency_df.loc[Constituency_df['g'] == x, 'e'].sum()
        list.append(y)
        y = (Constituency_df.g.values == x).sum()
        list.append(y)
        y = Constituency_df.loc[Constituency_df['g'] == x, 'f'].sum()
        list.append(y)

        # Last 3 entries in one row
        list.append(list[0]+list[3])
        list.append(list[1] + list[4])
        list.append(list[2] + list[5])

        District.loc[index[i]] = list
        i=i+1

    list = []
    for i in columns:
        y= sum(District[i])
        list.append(y)

    District.loc['Works Sanctioned'] = list
    return (District)


dis_vector = ['Rangareddy', 'Vikarabad','Medchal-Malkajgiri']

#Circle Function
def Circle(dis_vector):
    Circle_df = pd.DataFrame(data=0,
                                columns=['Length in kms(1000cr)', 'No. of works(1000cr)', 'Amount (Rs. In Lakhs)(1000cr)',
                                        'Length in kms(2500cr)', 'No. of works(2500cr)', 'Amount (Rs. In Lakhs)(2500cr)',
                                        'Length in kms(total)', 'No. of works(total)', 'Amount (Rs. In Lakhs)(total)'],
                                index=['Works Sanctioned', 'Works Completed', 'Works in progress',
                                        'Tenders received and Work about to be started',
                                        'Estimate stage/Tenders no response/Work not yet entrusted'])

    for i in dis_vector:
        Circle_df = Circle_df.add(District_Table(i))

    print(Circle_df.to_markdown())

Circle(dis_vector)
sys.stdout.flush()
