import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open(data, mode="r")
    d=csv.reader(f)

    return len((list(d))[1])
print(find_number_of_columns("data.csv"))

# Read the csv file