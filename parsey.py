import re

# Open the quiz file
with open('quiz.txt', 'r') as file:
    content = file.read()

# Split the content into individual questions
questions = re.split('Question [0-9]+\n', content)[1:]

# Loop through each question and extract the possible answers and correct answer
for question in questions:
    # Extract the question text
    match = re.search('(.+)\n', question)
    if match:
        q_text = match.group(1)
    
    # Extract the possible answers
    match = re.search('\n(.+)\n', question)
    if match:
        answers = match.group(1)
    
    # Extract the correct answer
    match = re.search('Correct!\n\s+(.+)\n', question)
    if match:
        correct_answer = match.group(1)
    
    # Replace the answer options with the correct answer
    new_question = re.sub('Correct!\n\s+(.+)\n', correct_answer, question)
    
    # Print the new question with correct answer
    print(f'{q_text} {answers}; {correct_answer}')
    
    # Write the new question with correct answer to file
    with open('mc.txt', 'a') as file:
        file.write(f'{q_text} {correct_answer}\n')
