import csv

# Read in the raw text from a file
with open("questions.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Split the raw text into individual questions
questions_raw = raw_text.split("UnansweredQuestion ")

# Remove the first element (it's empty)
questions_raw.pop(0)

# Parse each question into a dictionary
questions = []
for question_raw in questions_raw:
    # Split the question into lines
    lines = question_raw.strip().split("\n")
    
    # Check that there are at least two lines
    if len(lines) < 4:
        continue  # Skip this iteration of the loop and go to the next question
    
    # Extract the question and answer
    question = lines[2].strip()
    answer = lines[-1].strip()
    
    # Add the question and answer to the list of questions
    questions.append([question, answer])

# Write the questions and answers to a CSV file
with open("questions.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Question", "Answer"])
    for question in questions:
        writer.writerow(question)
