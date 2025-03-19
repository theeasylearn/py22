import os

# create a new directory
# os.mkdir('new')

print(os.getcwd())

# change directory
os.chdir('./new')

# os.mkdir("python")

# get current working directory
print(os.getcwd())

# remove a directory

# os.rmdir('python')

os.chdir('../')
print(os.getcwd())
os.rmdir('new')
# os.rmdir('myfolder')
