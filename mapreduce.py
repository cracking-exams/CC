# mapreduce_wordcount.py

from collections import defaultdict

# Mapper function
def mapper(text):
    words = text.split()
    for word in words:
        yield (word.lower(), 1)

# Reducer function
def reducer(mapped_data):
    word_count = defaultdict(int)
    for word, count in mapped_data:
        word_count[word] += count
    return word_count

# Main function
def main():
    text = """
    MapReduce is a programming model for processing large data sets
    with a distributed algorithm on a cluster.
    """
    # Map step
    mapped = list(mapper(text))
    
    # Reduce step
    reduced = reducer(mapped)

    # Output the results
    for word, count in reduced.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
