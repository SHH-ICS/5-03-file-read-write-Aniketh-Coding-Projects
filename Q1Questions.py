
with open("questions.txt", "a") as file:

    question = input("Enter the multiple-choice question: ")
    answer_a = input("Enter answer A: ")
    answer_b = input("Enter answer B: ")
    answer_c = input("Enter answer C: ")
    answer_d = input("Enter answer D: ")
    correct_answer = input("Enter the letter of the correct answer (A, B, C, or D): ")

    file.write(f"Question: {question}\n")
    file.write(f"A. {answer_a}\n")
    file.write(f"B. {answer_b}\n")
    file.write(f"C. {answer_c}\n")
    file.write(f"D. {answer_d}\n")
    file.write(f"Correct Answer: {correct_answer}\n\n")

print("Question saved to questions.txt!")
