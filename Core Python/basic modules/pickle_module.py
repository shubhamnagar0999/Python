#pickle module used to read and write python object in to binary file(pkl)
import pickle
l = [2,3,4,5,3,3,3,10,4,4,5]

with open("file.pkl","wb") as file:
    pickle.dump(l, file)           #is used to convert object to binary

with open("file.pkl","rb") as file2:
    print(pickle.load(file2))     # will covert binary to python object