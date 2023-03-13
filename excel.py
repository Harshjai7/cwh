import pandas as pd # This is the library for readind data from excel
file_path=' '# Give the file path of the excel
df = pd.read_excel(file_path)
excel_data = df.values
column_name =' ' #Give the pardicualar column 
selected_data= df[column_name]
print(selected_data) #this is for printing the data in compiler
