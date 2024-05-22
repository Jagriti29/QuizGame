print("Welcome to the Quiz Game!")
print("Instructions:")
print("1. You will be presented with multiple-choice questions.")
print("2. For each question, enter the letter corresponding to your answer.")
print("3. Each correct answer will give you +1 point.")
print("4. Each incorrect answer will deduct 0.5 points.")
print("5. Let's start the quiz!\n")

a = input("Do you want to play? Yes/No: ").lower()

if a == "yes":
    print("Let's begin!\n")
    print("Please choose a topic:")
    print("1. Science")
    print("2. General Knowledge")
    print("3. Current Affairs")

    topic_choice = input("Enter the number of your choice: ")

    if topic_choice == "1":
        score = 0

        print("What is the chemical symbol for water? a) H2O b) O2 c) CO2 d) H2 ")
        q1 = input("Your Answer: ").lower()
        if q1 == "a":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is H2O.")
            score -= 0.5
        print("Your current score is:", score)

        print("What planet is known as the Red Planet? a) Venus b) Mars c) Jupiter d) Saturn")
        q2 = input("Your Answer: ").lower()
        if q2 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Mars.")
            score -= 0.5
        print("Your current score is:", score)

        print("Which element is essential for the production of thyroid hormones in the human body? a) Iron b) Calcium c) Iodine d) Zinc")
        q3 = input("Your Answer: ").lower()
        if q3 == "c":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Iodine.")
            score -= 0.5
        print("Your current score is:", score)

        print("Which of the following is the most abundant gas in Earth's atmosphere? a) Oxygen b) Carbon dioxide c) Nitrogen d) Argon")
        q4 = input("Your Answer: ").lower()
        if q4 == "c":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Nitrogen.")
            score -= 0.5
        print("Your current score is:", score)

        print("Final score is:", score)
        
    elif topic_choice == "2":
        score = 0

        print("What is the smallest country in the world by land area? a) Monaco b) Nauru c) San Marino d) Vatican City ")
        q1 = input("Your Answer: ").lower()
        if q1 == "d":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Vatican City.")
            score -= 0.5
        print("Your current score is:", score)

        print("Which country is known as the Land of the Rising Sun? a)  China b) Japan c) South Korea d) Thailand")
        q2 = input("Your Answer: ").lower()
        if q2 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Japan.")
            score -= 0.5
        print("Your current score is:", score)

        print("In which year did the Titanic sink? a) 1910 b) 1912 c) 1914 d) 1916")
        q3 = input("Your Answer: ").lower()
        if q3 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is 1912.")
            score -= 0.5
        print("Your current score is:", score)

        print("What is the longest river in the world? a) Amazon River b) Nile Rive c) Yangtze River d) Mississippi River")
        q4 = input("Your Answer: ").lower()
        if q4 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Nile Rive.")
            score -= 0.5
        print("Your current score is:", score)

        print("Final score is:", score)

    elif topic_choice == "3":
        score = 0

        print("Which tech company recently became the first to reach a market valuation of $3 trillion in 2024? a) Apple b) Microsoft c) San Google d) Amazon ")
        q1 = input("Your Answer: ").lower()
        if q1 == "a":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Apple.")
            score -= 0.5
        print("Your current score is:", score)

        print("What significant event did the United Nations declare for May 21, 2024? a) World Peace Day b)  International Day for Biological Diversity c) World Health Day d) International Tea Day")
        q2 = input("Your Answer: ").lower()
        if q2 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is International Day for Biological Diversity.")
            score -= 0.5
        print("Your current score is:", score)

        print("Which Indian public sector bank recently launched its 'Digital Banking Units' (DBUs) to enhance customer service in rural areas? a) State Bank of India b) Punjab National Bank c)  Bank of Baroda d)  Union Bank of India")
        q3 = input("Your Answer: ").lower()
        if q3 == "a":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is State Bank of India.")
            score -= 0.5
        print("Your current score is:", score)

        print("Which Indian state recently launched the 'Mukhyamantri Ladli Bahna Yojana' to provide financial assistance to women? a) Uttar Pradesh b) Madhya Pradesh c) Bihar d) Rajasthan")
        q4 = input("Your Answer: ").lower()
        if q4 == "b":
            print("Correct answer!")
            score += 1
        else: 
            print("Incorrect! The correct answer is Madhya Pradesh.")
            score -= 0.5
        print("Your current score is:", score)

        print("Final score is:", score)

else:
    print("Okay!Have a nice day.")



