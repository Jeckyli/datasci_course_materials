import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

def reducer(key, list_of_values):
    b_count = {}
    for b in list_of_values:
        b_count.setdefault(b, 0)
        b_count[b] += 1
    for b in b_count:
        if b_count[b] == 1:
            mr.emit((key, b))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
