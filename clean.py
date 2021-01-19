from os import remove

# try:
#     # remove("output.txt")
# except:
#     pass
try:
    remove("database.db")
except:
    pass
