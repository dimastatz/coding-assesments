# Part 1: Python Multiprocessing

## Objectives
Write a small Python application with two processes, running on the same machine. The two processes will communicate over a socket. (Randomly generated) vectors from the first process will be sent to the second process. These “data” vectors should be accumulated in the second process in a matrix. Some simple statistics will be computed (across the “temporal” dimension). Results should be saved to a file ...
- [click to see the full task description](./part_1.md)

## HOW TO

### Github:
Clone the Github repo 
```bash 
git clone git@github.com:dimastatz/coding-assesments.git
```

### Working Folder:
Navigate to py-multproc folder
```bash 
cd coding-assesments/cogntiv/part1/py-multiproc/ 
```

### Python Version
Check the installed python3 version
```bash 
python3 -V 
```
This project is tested on Python 3.10.0. It should work OK on python 3.6+

### NumPy
This project uses standard Python modules and [numpy](https://numpy.org/). Ensure that the numpy is installed by running 
```Python
import numpy
print numpy.__version__
```
If not installed, install it by running
```bash
pip3 install numpy
```

### Run the code
 Run the code by
```bash
python3 main.py add_noise
```
or run it without noise
```bash
python3 main.py
```

### Output
The code prints stats to the stdout and file. The file will be created in the current directory. Please
ensure that the folder has RW permissions. 

### Problems
Do not hesitate to contact me if you see any problems.



