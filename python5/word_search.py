data = True

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()
        
        if("python" in data):
            print("word found")
            break
        print( data)