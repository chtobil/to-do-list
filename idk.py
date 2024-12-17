def add_task(list):
    xD = input("Введите задачу: ")
    list.append(xD)

def show_tasks(list):
    for i in range(len(list)):
        print(i+1 , list[i])
