
import random
class user:

    def __init__(self, name, score=0):
        self.name = name
        self._score = score

class game:

    def __init__(self, user):
        self.user = user
        user._score 

    def question(self):
        questions = [
            {"Question": "What is your name", "Answer": "4"},
            {"Question": "What is 2 + 2", "Answer": "4"},
            {"Question": "What is 2*2", "Answer": "4"}
        ]
        self.count = 0
        while self.count < 4:
            a = random.choice(questions)
            print(a["Question"])
            answer = input("Enter your answer ")
            if answer == a["Answer"]:
                self.user._score += 1
                print("correct answer")
            else:
                print("Incorrect answer")
            self.count += 1

    def total_scores(self):
        total_scores = f"{self.user._score}/{self.count}"
        print(total_scores)
    def total_scroe(self):
        if self.user._score == 5:
            print("5/5, Excellent ")
        elif self.user._score == 4:
            print ("4/5, Good ")
        elif self.user._score == 3:
            print ("3/5, nice ")
        elif self.user._score == 2:
            print ("2/5, fair ")
        elif self.user._score == 1:
            print ("1/5,  worst")
        else:
            print("Failed 🤣🤣🤣")

    @property
    def score(self):
        return self.user._score
    

    
            

        


User1 = user("Heritage")
game1 = game(User1)
game1.question()
print(game1.score)
game1.total_scores()



