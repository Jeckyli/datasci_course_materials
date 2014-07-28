import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    for order in list_of_values:
        for item in list_of_values:
            if(order[0] == "order" and item[0] == "line_item"):
                mr.emit(order+item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
