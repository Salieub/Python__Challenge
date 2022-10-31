import csv
from itertools import count
with open("Resources/budget_data.csv") as csvfile:
     csvreader= csv.reader(csvfile,delimiter=",")
     csv_header=next(csvreader)
     first_row=next(csvreader)
     count=1
     total=int(first_row[1])
     changes=int(first_row[1])
     totalnet=0
     greatest_increase=["",0]
     greatest_decrease=["",999999999999]
     for row in csvreader:
      count=count+1
      total=total+int(row[1])
      totalnet=int(row[1])-changes
      changes=int(row[1])
      if totalnet>greatest_increase[1]:
         greatest_increase[0]=row[0]
         greatest_increase[1]=totalnet
      if totalnet<greatest_decrease[1]:
         greatest_decrease[0]=row[0]
         greatest_decrease[1]=totalnet
        
entireperiod=totalnet/count
print(count)
print(total)
print(entireperiod)
print(greatest_increase)
print(greatest_decrease)



     
  

   