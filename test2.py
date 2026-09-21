def question():
        question = [
            {"Question": "What is your name", "Answer": "Heritage"},
            {"Question": "What is 2 + 2", "Answer": "4"},
            {"Question": "What is 2*2", "Answer": "4"}
        ]
        for q in question:
            print(q["Answer"])
question()