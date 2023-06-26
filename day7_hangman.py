import random
print("WELCOME TO THE HANGMAN GAME")
print("INSTRUCTIONS: ")
print("You hav to choose a letter if that letter is found in the word chosen randomly bt system then go ahead otherwise you man will be hanged till death. ")
print("You have 5 Lives in this game")
print("That's All, Let's Start the game......")
print("HINT: These words are oftenly used in college days. ")
word_list = ['chill', 'party', 'midterms', 'coffee', 'assignments', 'hangout', 'exams', 'notes', 'procrastinate', 'dorm', 'lecture', 'club', 'library', 'weekend', 'study', 'break', 'homework', 'roommate', 'campus', 'essay', 'quiz', 'scholarship', 'presentation', 'textbook', 'research', 'deadline', 'professor', 'major', 'minor', 'gpa', 'advisor', 'tuition', 'classroom', 'career fair', 'commencement', 'transcript', 'loan', 'plagiarism', 'networking', 'alumni', 'thesis', 'undergraduate', 'graduate', 'dissertation', 'placement']

chosen_word = random.choice(word_list)
l = len(chosen_word)

aa = []
for _ in range(l):
    aa +="_"
print(aa)
lives = 5
hangman_fig = [
    "   ____",
    "  |    |",
    "  |    O",
    "  |   /|\\",
    "  |    |",
    "  |   / \\",
    "__|__",
]
while lives > 0 and "_" in aa:
    lett = input("Guess a letter: ").lower()
    found = False
    if lett in aa:
        print("You have already guessed ",lett)
    else :
        for i in range(l):
            if lett == chosen_word[i]:
                aa[i] = lett
                found = True
        if not found:
            lives -= 1
            print("Sorry, LIVES LEFT = ",lives)
            print("\n".join(hangman_fig[:6 - lives]))
            continue
        print(aa)
    

if "_" not in aa:
    print("Congratulations! You won!!!.")
else:
    print("Game over. You ran out of lives.")
    print ("The Word was : ", chosen_word)

