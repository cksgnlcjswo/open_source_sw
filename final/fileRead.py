from csv import reader

def converToFlaot(row):
  ret=[]
  for tmp in row:
    ret.append(float(tmp))
  return ret

def loadData():
# skip first line i.e. read header first and then iterate over each row od csv as a list
    pos = []
    with open('scp_data.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                coord = converToFlaot(row)
                pos.append(coord)

    print("loaded ", len(pos)," data!")
    return pos
                