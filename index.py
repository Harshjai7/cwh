import pandas as pd
file_path = 'C:/xampp/htdocs/cwh/test.csv.xlsx'
df = pd.read_excel(file_path)
excel_data = df.values
column_name ='username'
selected_data= df[column_name]
column_name ='password'
selected_data1= df[column_name]
print(selected_data)
