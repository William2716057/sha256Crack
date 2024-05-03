# SHA-256 Hash Collision Finder
This Python script is designed to find a partial string that, when combined with a given partial string, generates a SHA-256 hash equal to a target hash.

## Usage
### Requirements
1. Python 3.x installed on your system.

## Getting Started
1. Download or clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Open the script in a text editor or IDE of your choice.
4. Customize the partial variable with your desired partial string.
5. Set the targetHash variable with the SHA-256 hash of the full string you're trying to find.

Run the script.

python sha256Crack.py

## How It Works
The script iterates through all possible characters to generate different combinations of the partial string with an appended character. 
For each combination, it calculates the SHA-256 hash and compares it with the target hash. If a match is found, the matched string is displayed.
