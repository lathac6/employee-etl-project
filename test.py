# import pandas as pd
# df = pd.read_csv('employees.csv')
# print('original file')
# print(df)
# df['salary']=df['salary'].fillna(0)
# df= df.drop_duplicates()
# print(df)
# df = df.to_csv('employees2.csv')
# # print('9',df)
# import pandas as pd
# df = pd.read_csv('employees.csv')
# print(df)
# df = df[df["salary"] > 25000]
# df = df.to_csv('high_employessalary.csv')
# # print('15',df)
# import pandas as pd
# df = pd.read_csv('employees.csv')
# df = df.rename(columns={"emp_id":"id",
#               "emp_name":"name",
#               "emp_salary":"salary"})
# df = df.to_csv('cleaned_columss.csv',index=False)
# print('22',df)
# import pandas as pd
# df =pd.read_csv('employees.csv')
# sorted_df = df.sort_values(by="salary",ascending=False)
# print('26',sorted_df)
# df= sorted_df.to_csv('sorted_data.csv',index=False)\
# import pyarrow as pa
# import pyarrow.parquet as pq

# # Create a sample table
# table = pa.Table.from_pydict({
#     'id': [1, 2, 3],
#     'product': ['apple', 'banana', 'carrot'],
#     'price': [1.5, 0.5, 1.0]
# })

# # Write to parquet
# pq.write_table(table, 'example.parquet')

# # Read back
# parquet_table = pq.read_table('example.parquet')
# print(parquet_table)

# import pandas as pd 
# df = pd.read_csv('employees.csv')
# print('47',df.dtypes)
# df['salary'] = df['salary'].astype('int')
# newdf= df.to_csv('datatypeconvestion.csv')
# print(newdf.dtypes)
import pandas as pd
df = pd.read_csv('datatypeconvestion.csv')
print('53',df.dtypes)
df['id']=df['id'].astype('str')
print('df',df.dtypes)