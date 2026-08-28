Tasks = []

def add_task(Description):
    new_task = {"description": Description, "done": False}
    Tasks.append(new_task)
    return new_task
add_task("Attend To Meetings",)
add_task("Reach out to CEO")
add_task("code with claude")
def view_task():
    for index, Task in enumerate(Tasks, start=1):
        if Task["done"]:
            status = "done"
        else:
            status = "Not done"
        print(f"{index}. {Task['description']} - {status}")
def complete_task(task_number):
    done_task = Tasks[task_number -1]["done"] = True
    return done_task
def delete_task(task_number):
    updated_task = Tasks.pop(task_number -1)
    return updated_task
complete_task(1)
complete_task(2)
complete_task(3)
delete_task(2)
view_task()