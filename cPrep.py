# tool for compiling C++ programs written in C++

import os


itemName = input('type name of file')

os.system("g++ -o " + itemName + " " + itemName + ".cpp")
print('compiled')
os.system("./" + itemName)
    
