import py_compile
filename = input("""what is the file name (Include the .py)
""")
try:
    py_compile.compile(filename)
except:
    print("Please make sure the file is in the same location as this script")
