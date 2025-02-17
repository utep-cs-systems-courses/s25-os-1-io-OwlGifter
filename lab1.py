import os
import re
import sys

def read_file(fd):
    # reads file using bytes
    content = b""
    while True:
        chunk = os.read(fd, 4096)
        if not chunk:
            break
        content += chunk
    return content.decode("utf-8")

def write_file(fd, data):
    # writes data to file
    os.write(fd, data.encode("utf-8"))

def count_words(text):
    # counts words using find all, and turning all words to lower
    words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())
    word_count = {}
    for word in words:
        if word in word_count.keys():
            word_count[word] +=1
        else:
            word_count[word] = 1
    return word_count

def main():
    if len(sys.argv) != 3:
        print("Not Enough Arguements")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    try:
        input_fd = os.open(input_filename, os.O_RDONLY)
    except OSError as e:
        print("Error on file opening part")
        sys.exit(1)
    
    text = read_file(input_fd)
    os.close(input_fd)
    
    word_counts = count_words(text)
    
    sorted_words = sorted(word_counts.items())
    output_data = "\n".join(f"{word} {count}" for word, count in sorted_words) + "\n"
    
    try:
        output_fd = os.open(output_filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    except OSError as e:
        print("Error with output file thing")
        sys.exit(1)
    
    write_file(output_fd, output_data)
    os.close(output_fd)
    
if __name__ == "__main__":
    main()
