import io
import csv

def parse_result(r, result):
    with io.StringIO(r, newline='') as rf:
        reader = csv.reader(rf, delimiter=':', skipinitialspace=True)
        for row in reader:
            if len(row) < 4:
                pass
            elif row[0] == 'K':
                result[row[1]] = { 
                        'type': 'K', 
                        'name': row[2], 
                        'votes': row[3] 
                        }
            elif row[0] == 'V':
                result[row[1]]['lokal'] = { 
                        'type': 'V', 
                        'name': row[2], 
                        'votes': row[3] 
                        }
            elif row[0] == 'R':
                result[row[1]][row[2]] = { 
                        'type': 'R', 
                        'party': row[2], 
                        'votes': row[3], 
                        'pct': row[4] 
                        }
            else:
                pass

    return result
