# code also submitted via GitHub
import pandas as pd 

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

# ***  Table Setup *** 
# Splitting delimited data into rows and columns
split_by_rows = data.split('\n')
split_by_columns = []
for row in split_by_rows:
    split_by_columns.append(row.split(';'))
  
# Calling DataFrame constructor  
flight_table = pd.DataFrame(split_by_columns[1:-1], columns = split_by_columns[0])  

# *** Q1 *** 
# Function to convert existing flight codes to Integers and add missing codes in
flight_code_counter = int(float(flight_table.FlightCodes[0]))
def fix_flight_codes(code):
    global flight_code_counter
    if code == '':
        flight_code_counter += 10
        return flight_code_counter
    flight_code_counter = int(float(code))
    return flight_code_counter

# Apply function to each flight code in the table 
flight_table['FlightCodes'] = flight_table['FlightCodes'].apply(fix_flight_codes)

# ***  Q2 *** 
# Split the To_From column and drop the old one
flight_table[['To', 'From']] = flight_table['To_From'].str.split('_', expand=True)
flight_table.drop('To_From', axis=1, inplace=True)

# Apply correct capitalization
flight_table['To'] = flight_table['To'].apply(lambda location: location.capitalize())
flight_table['From'] = flight_table['From'].apply(lambda location: location.capitalize())

# ***  Q3 *** 
# Method that leaves only spaces and alpha characters in the airline code string
def fix_punc(airline):
    punc_fixed = ""
    for char in airline:
        if char.isalpha() or char.isspace():
            punc_fixed += char
    
    return punc_fixed

flight_table['Airline Code'] = flight_table['Airline Code'].apply(fix_punc)

# *** Q4 ***  
# - Note: No flights departing from Waterloo are present in the inital data string

#Pandas Query: 
print(flight_table.loc[flight_table['From'] == 'Waterloo']) # returns an empty data frame

# SQL Query:
'''
SELECT * 
FROM flight_table
WHERE flight_table.From = 'Waterloo'
'''

print(flight_table)
'''
Airline Code    DelayTimes      FlightCodes        To       From
0      Air Canada       [21, 40]        20015  Waterloo    Newyork
1      Air France             []        20025  Montreal    Toronto
2  Porter Airways   [60, 22, 87]        20035   Calgary     Ottawa
3       Air France      [78, 66]        20045    Ottawa  Vancouver
4        Lufthansa      [12, 33]        20055    London   Montreal
''' 