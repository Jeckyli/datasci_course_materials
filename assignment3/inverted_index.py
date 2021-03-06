import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: word in book content
    # value: document id
    words = record[1].split()
    for w in words:
      mr.emit_intermediate(w, record[0])

def reducer(key, list_of_values):
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
