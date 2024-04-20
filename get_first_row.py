import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """

   f=open(data, mode='r')
   k=csv.reader(f)
   a=[]
   for i in list(k):
      a.append(i[0])
   
   return a
print(get_first_row('data.csv'))

# Read the csv file