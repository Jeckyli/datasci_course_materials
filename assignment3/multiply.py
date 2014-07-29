import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    for a in record:
        if (a[0] == "a"):
            mr.emit_intermediate(a[1],i), (a[2], a[3])
        sum = 0;
        for b in record:
            if(a[0] == "a" and b[0] == "b" and a[2] == b[1]):
                sum +=
        ((a[1], b[2]), a)        

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
