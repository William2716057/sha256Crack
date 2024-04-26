
import hashlib
from imghdr import tests

def calculateHash(inputString):
    inputBytes = inputString.encode('utf-8')
    sha256Hash = hashlib.sha256(inputBytes).hexdigest()
    return sha256Hash

partial = "samplekeywor"
targetHash = calculateHash("samplekeyword")
print("Target Hash: ", targetHash)
found = False

for i in range(256):
    testString = partial + chr(i)
    testHash = calculateHash(testString)
    
    if testHash == targetHash:
        print("Match found: ", testString)
        found = True
        break
    
if not found:
    print("No match found")