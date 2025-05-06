import sys

def FindTheWord(file_path, search_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = []
            for line in f:
                if search_word.lower() in line.lower():
                    lines.append(line)
        return lines
    except FileNotFoundError:
        print(f"Attention! File {file_path} wasn't found. Check the path or create new file and try again!")
    except Exception as e:
        print(f"Attention! Error: {e}")
                
def PrintFoundString(found_strings):
    if found_strings:
        for line in found_strings:
            print(line)
    else:
        print(f"'{word}' wasn't found in {f_path}")

if len(sys.argv) !=3:
    print("Run pattern is: 'python word_finder.py <path_to_your_file> <word>'")
    sys.exit(1)


f_path = sys.argv[1]
word = sys.argv[2]

PrintFoundString(FindTheWord(file_path=f_path, search_word=word))


