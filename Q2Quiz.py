score = 0
total_questions = 0

try:
    with open("questions.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 6):
        if i + 5 >= len(lines):
            break

        question = lines[i].strip()[10:]
        answer_a = lines[i + 1].strip()
        answer_b = lines[i + 2].strip()
        answer_c = lines[i + 3].strip()
        answer_d = lines[i + 4].strip()
        correct_answer = lines[i + 5].strip()[-1]  

        print(f"\n{question}")
        print(answer_a)
        print(answer_b)
        print(answer_c)
        print(answer_d)

        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

        total_questions += 1

    print(f"\nYou answered {score} out of {total_questions} questions correctly.")

except FileNotFoundError:
    print("Error: The file 'questions.txt' was not found. Please ensure it exists in the same directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
