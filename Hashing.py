
# Function that hashes a string into a number
# using Java's hashing function
def hashString(key: str, n: int) -> int:
    if key is None:
        raise Exception("Key cannot be empty.")
    h: int  = 0 # hash value to be computed for key
    for i in range(len(key)):
        h = (31*h) + ord(key[i])
    return h % n

def main():
    words: list = ["apple", "banana", "cherry", "date", "elderberry",
                "fig", "grape", "honeydew", "imbe", "jackfruit",
                "kiwi", "lemon", "mango", "nectarine", "orange"]
    N: list = [0] * 100 # Array of length 100 for modulus 
    for word in words:
        print(f"{word} hashes to {hashString(key=word, n = len(N))}")

if __name__ == "__main__":
    main()