with open('questions.csv', 'r', encoding='utf-8') as file_in, open('evan.txt', 'w', encoding='utf-8') as file_out:
    for line in file_in:
        last_comma_position = line.rfind(',')
        if last_comma_position != -1:  # Check if a comma was found in the line
            line = line[:last_comma_position] + ';' + line[last_comma_position + 1:]
        file_out.write(line)
