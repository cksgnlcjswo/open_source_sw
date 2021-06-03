'''
    description : csv 파일 읽기 
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com   
'''

from csv import reader

'''행을 읽어와서 float형으로 cast'''
def converToFlaot(row):
  ret=[]
  for tmp in row:
    ret.append(float(tmp))
  return ret

'''csv파일에서 데이터 읽어오기. 첫번째 행은 X0,X1이므로 제외'''
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
                