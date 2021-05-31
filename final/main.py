from csv import reader
pos=[]

def converToFlaot(row):
  ret=[]
  for tmp in row:
    ret.append(float(tmp))
  return ret

# skip first line i.e. read header first and then iterate over each row od csv as a list
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
            
#print(pos)
#print(len(pos))

#현재 점들의 위치 좌표 보여주기
import matplotlib.pyplot as plt

x, y = zip(*pos)
plt.scatter(x, y)
plt.show()
