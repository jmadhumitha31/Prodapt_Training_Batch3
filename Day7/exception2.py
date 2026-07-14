def read_file(filename):
    try:
        file=open(filename,'r')
        date=file.read()
        print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found")
    except IOError:
        print("Error occured while reading the file")
    finally:
        file.close()

readfilename=input("Enter the filename to read")
read_file(readfilename)