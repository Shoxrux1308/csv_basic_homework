import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open(data, mode='r')
    k=csv.reader(f)

    return list(k)[1]
print(get_first_column('data.csv'))
    
# Read the csv file