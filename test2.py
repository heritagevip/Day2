
class mini_framework:
    def __init__(self):
        self.tasks =[]
    
    def register(self, func):
        self.tasks.append(func)

    def run(self):
        print("Framework starting")
        for task in self.tasks:
            task()
        print("Framework done")


app = mini_framework()

def my_logic():
    print("Doing something i dont understand")

def anoother_task():
    print("i dont understand at all")

app.register(my_logic)
app.register(anoother_task)
app.run()