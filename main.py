from tasks import add_task, list_tasks, mark_done
def main():
    print("Welcome to To-Do List Lite")

    while True:
        answer = input("\nchose (add/list/done/exit): ").strip().lower()

        if answer == "add":
            add_task()

        elif answer == "list":
            list_tasks()

        elif answer == "done":
            mark_done()
        
        elif answer == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid answer. Please choose add, list, done, or exit.")

if __name__ == "__main__":
    main()
