from idk import add_task , show_tasks
from dele import del_all, del_task

def handle_command(ans: int, list):
    if ans == 1:
        add_task(list)
    elif ans == 2:
        del_task(list)
    elif ans == 3:
        show_tasks(list)
    elif ans == 4:
        del_all(list)
    else :
        exit()


def print_menu():
    print("=== Меню ===") # Done
    print("1. Добавить задачу ") # Done
    print("2. Удалить задачу ") # done
    print("3. Посмотреть все задачи ") # Done
    print("4. Очистить список задач") # done
    print("5. Выход") #Done


def read_ans():
    ans = int(input("Выберите действие: "))
    if ans < 1 or ans > 5:
        print("ERROR: Нет опции")
        return None
    return ans


def main() :
    list = []
    while True:
        print_menu()
        ans = read_ans()
        if ans == None:
            exit()
        handle_command(ans,list)





if __name__ == "__main__":
    main()