tasks = {}

with open('todo.txt', 'r+', encoding='utf-8') as file:
    todo = file.readlines()
    for line in todo:
        task, status = line.split(": ")
        tasks[task] = status.strip()

if len(tasks.keys()) == list(tasks.values()).count('DONE'):
    print("Всё сделано!")
else:
    print(f"В списке {len(tasks.keys())} дел\n"
          f"Сделано {list(tasks.values()).count('DONE')} из {len(tasks.keys())}\n"
          f"Давай пройдемся по твоим делам!\n")

    for task, status in tasks.items():
        if status == "TODO":
            answer = input(f"{task} - сделано? (y/n)\n").strip().lower()
            if answer == "y":
                tasks[task] = "DONE"

    with open('todo.txt', 'w', encoding='utf-8') as file:
        for task, status in tasks.items():
            file.writelines(f"{task}: {status}\n")

    print("Список дел обновлен, смотри файл")
