from pathlib import Path

birthday = input("Type in your birth date in the ddmmyyyy or ddmmyy format: ")
path = Path('pi_million.txt')
contents = path.read_text()
lines = contents.splitlines()
exists = 0
searched = False
while exists == 0 and searched == False:
    for line in lines:
        if birthday in line:
            exists = 1
    break
        

print ("Your birthday is in the first 1000001 numbers of the pi number!" if exists == 1 else "Your birthday is not in the first 1000001 numbers of the pi number :(")