import timeit

DataList = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000)
DataTuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)

print("waktu untuk memproses list ", DataList)
print("waktu untuk memproses tuple", DataTuple)

