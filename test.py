

capture = open("conf.txt", "r")

textFromFile = capture.read()

arrayFile = textFromFile.split('\n') # Split the text from file by new line "\n" < -- new line and append every line into array element ['...','...'...]
arrayNew = []
a = 0
i = 0

for x in arrayFile:  # Cicle over array arrayFile. Every element from array is in "x"
    a += 1           # increment a by 1
    if "crypto map" in x:   # Checks "x" for "crypto map"
        arrayNew.append(arrayFile[a - 1]) # if has "crypto map" add the element into new array
    if "description" in x:    # Same just looking for "description"
        arrayNew.append(arrayFile[a - 1])
    if "set transform-set" in x:   # Same just looking for "set transform-set"
        arrayNew.append(arrayFile[a - 1])
        # print(arrayNew)
for el in arrayNew:     # Cicle over the new created array arrayNew which has just "crypto map" "description" and "set transform-set" for every tunnel conf in row
    i += 1              # increment a by 1
    if "set transform-set " in el:  # Checks "el" for "set transform-set "
        res = el.split('set transform-set ') # Split the text from "el" by "set transform-set " to take just the text after "set transform-set "
        if "aes256-sha" not in res[1]: # Check for "aes256-sha" not in "el" res[1]
            {
                print(
                    " This tunnels doesn't have aes256-sha256 or aes256-sha at transform-set -- > ", arrayNew[i - 2]) # Print "description" two elements back from array arrayNew
            }
