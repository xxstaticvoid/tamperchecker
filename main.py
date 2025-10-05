#!/usr/bin/env python3
import csv
import hashlib
import os
import sys

HASH_FILE = 'saved_hashes.csv'


def compute_hash(filename) -> str:
    md = hashlib.sha256()
    with open(filename, "rb") as file:
        while chunk := file.read(1024): #1 kb
            md.update(chunk)
        return md.hexdigest()


def save_hash(filename, hash_val, hash_file = HASH_FILE) -> None:
    with open(hash_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([filename, hash_val])


def check_tamper(filename, hash_file = HASH_FILE) -> int:

    current_hash = compute_hash(filename)

    if not os.path.exists(hash_file):
        #make file
        with open(hash_file, 'x') as file:
            pass

    with open(hash_file, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if len(row) == 0:
                break
            if row[0] == filename:
                if row[1] != current_hash:
                    return 1
                else:
                    return 2
            
    #not if file
    save_hash(filename, current_hash)
    return 3


def main():


    #Check cli arguments
    if len(sys.argv) != 2:
        print("Needs name of file")
        sys.exit(1)

    filename = sys.argv[1]

    #check if file to check exists
    if not os.path.exists(filename):
        sys.exit("File not found")


    result = check_tamper(filename)
    if result == 1:
        print(f"{filename} has been changed")
    elif result == 2:
        print(f"{filename} has not been changed")
    elif result == 3:
        print(f"{filename} has been set")

    sys.exit(0)

if __name__ == "__main__":
    main()
