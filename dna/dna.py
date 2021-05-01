from csv import reader, DictReader
from sys import argv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(0)
else:
    csv_name=argv[1]
    txt_name=argv[2]

dna_inp=[]

with open(txt_name,"r") as file:
    dna_inp = file.read().strip()

dna_dict = {}

with open(csv_name,"r") as file: # creates dna_types string 
    csv_reader= reader(file)
    for row in csv_reader:
        dna_types = row
        dna_types.pop(0)
        break


for item in dna_types: #creates the dictionary in which the keys will be the maximum repetition counts
    dna_dict[item] = 1

for dna_type in dna_dict: # counting through the types of dna to be scanned for
    l = len(dna_type)
    Max_reps = 0 # Max repetition count
    n = 0
    for i in range(len(dna_inp)): #counting through input dna sequence
        while n > 0:
            n -= 1
            continue
        if dna_inp[i: i + l] == dna_type:
            while dna_inp[i - l: i] == dna_inp[i: i + l]:
                n += 1
                i += l #skips by the number of letters of that particular dna type
            if n > Max_reps:
                Max_reps=n
    
    dna_dict[dna_type] += Max_reps #makes the key of the dictionary as the max repetitions of that particular dna type


with open(csv_name, newline='') as file:
    people = DictReader(file)
    for person in people:
        match = 0
        for dna in dna_dict:
            if dna_dict[dna] == int(person[dna]): #compares the particular dna_type count of a particular person with the max repetition count of the particular dna type
                match += 1
        if match == len(dna_dict):
            print(person['name'])
            exit(0)

    print("No match")