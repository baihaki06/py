import sys

DataList = [1,2,3,4,5,6,7,8,"pisang rebus", "jahe susu", "duren", "ketan", False, 3.14]
DataTuple = (1,2,3,4,5,6,7,8,"pisang rebus", "jahe susu", "duren", "ketan", False, 3.14)

BesarDataList = sys.getsizeof(DataList)
BesarDataTuple = sys.getsizeof(DataTuple)

print("Besar data List ", BesarDataList)
print("Besar data tuple ", BesarDataTuple)

