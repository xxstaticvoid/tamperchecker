# tamperchecker
Save files as is and compare them in the future to see if a file has been changed. 


Utilizes **hashlib** to generate a message digest from the SHA-256 hash function. This is commonly used for digital footprint and acts to verify the integrity and authenticity of data. Hash functions like SHA-256 are really great due their collision resistantance especially when compared against the eairlier SHA-1 and MD5. For this project I store the generated message digest for a text file into a csv file along with the name of the file. Then later, if I want to verify that one of my fiiles hasn't been changed I simply generate a new message digest from the same hash function and compare it with the one that was stored previously in the csv file. 
