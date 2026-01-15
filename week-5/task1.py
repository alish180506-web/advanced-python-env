import string

def analyze_text(input_file, output_file):
    # читаем файл
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    word_freq = {}

    # обрабатываем строки
    for line in lines:
        line = line.lower()
        line = line.strip()
        line = line.translate(str.maketrans("", "", string.punctuation))
        words = line.split()

        word_count += len(words)

        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # записываем результат
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Total lines: {line_count}\n")
        file.write(f"Total words: {word_count}\n")
        file.write("Word frequency:\n")
        for word, count in word_freq.items():
            file.write(f"{word}: {count}\n")

# запуск программы
analyze_text("text.txt", "analysis.txt")
