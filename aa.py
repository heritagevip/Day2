Tasks = []

def add_task(Description):
    new_task = {"description": Description, "done": False}
    Tasks.append(new_task)
    return new_task

def view_task():
    for index, Task in enumerate(Tasks, start=1):
        if Task["done"]:
            status = "done"
        else:
            status = "Not done"
        print(f"{index}. {Task['description']} - {status}")

add_task("Attend To Meetings",)
add_task("Reach out to CEO")
view_task()
add_task("Read ")
view_task()
add_task("Code with claude")
view_task()