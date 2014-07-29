import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    if (record[0] == "a"):
        for i in range(0, 5):
            mr.emit_intermediate((record[1],i), (record[2], record[3]))
    if (record[0] == "b"):
        for j in range(0, 5):
            mr.emit_intermediate((j,record[2]), (record[1], record[3]))

def reducer(key, list_of_values):
    temp = {};
    value = 0;
    for item in list_of_values:
         temp.setdefault(item[0], 1)
         if(temp[item[0]] != 1):
             value += temp[item[0]] * item[1]
         temp[item[0]] *= item[1]
    mr.emit((key[0], key[1] , value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
