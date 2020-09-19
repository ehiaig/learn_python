
import calendar
import pandas as pd

"""
Question:
The twenty-first century began on 1 January 2001 (a Monday) and will
end on 31 December 2100 (a Friday). What percentage of twenty-first
century Wednesdays fall on the last day of a month? (This question may
require some coding.)

Solution: 
1. Create an array of total wednesdays and Get the count.
2. Get the last day of first month, if it's a wednesday, add the day to an empty array.. 
keep looping thorugh the date range till all the months are done.
3. Get a count last_wednesdays
4. Answer = (Last wednesdays * 100)/total_wednesdays

"""
#Get list of wednesdays bewteen 2001-01-01 and 2100-12-31 
total_wednesdays_in_century = [d for d in pd.date_range(start="2001-01-01", end="2100-12-31") if d.weekday() in [2]]

# Now Get the lenght of all_wedmesdays = 5218
print(len(total_wednesdays_in_century))


#create an empty list containing all of last_wednedsdays bewteen 2001-01-01 and 2100-12-31 
last_wednesdays = []
    
#Create a list of months bewteen 2001-01-01 and 2100-12-31
for each_month in pd.date_range('2001-01-01','2100-12-31', freq='MS').tolist():
    
    #Using monthrange(), get the last day of each month
    last_day_of_month = each_month.replace(day = calendar.monthrange(each_month.year, each_month.month)[1])
    
    #Convert the result to Weekday using weekday()
    actual_result = calendar.day_name[last_day_of_month.weekday()]
    
    if actual_result == 'Wednesday':
        list_wed = last_wednesdays.append(each_month)
#         print("Given date:", each_month, "Last day of month:", actual_result)
print(len(last_wednesdays))


percentage_wednesday = (len(last_wednesdays) * 100) / len(total_wednesdays_in_century)
print("Percentage of twenty-first century Wednesdays that fall on the last day of a month is:", percentage_wednesday)



#Count the number of wednesdays between the given dates
# import numpy as np
# print(np.busday_count(begindates='2001-01-01', enddates='2100-12-31', weekmask='Wed'))