def getdata(e):
    import csv
    with open(e,'r') as f:
        reader = csv.reader(f)
        arr = [list(map(float,row)) for row in reader]
        length = len(arr)
        return arr,length
