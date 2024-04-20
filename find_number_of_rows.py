import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=open(data, mode='r')
    k=csv.reader(f)

    return len(list(k))
print(find_number_of_rows('data.csv'))

# Read the csv file
