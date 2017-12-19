import io
import csv

def parse_vallokal(vl):
    vallokal = { }
    with io.StringIO(vl, newline='') as vlf:
        #print("vlf")
        reader = csv.reader(vlf, delimiter=':', skipinitialspace=True)
        for row in reader:
            #print(row)
            if len(row) <= 1:
                pass
            elif row[0] == 'L':
                vallokal[row[1]] = { 'type': 'L', 'name': row[2] }
            elif row[0] == 'K':
                vallokal[row[2]] = { 'type': 'K', 'id': row[1], 'name': row[3] }
            elif row[0] == 'V':
                vallokal[row[2]] = { 'type': 'V', 'id': row[1], 'name': row[3] }
            else:
                pass

    return vallokal
        

