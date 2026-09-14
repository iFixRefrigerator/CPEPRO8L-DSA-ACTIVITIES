prompt = "~~~MAIN MENU~~~\n"
prompt += """1. Stack Operations (LIFO)
2. Queue Operations (FIFO)
0. Exit \n>>> """

active = True
while active:

    # get main menu choice safely
    while True:
        try:
            message = int(input(prompt))
            break
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")

    pushed_ch = []  # reset per main menu entry

    while message == 1:
        print("~~STACK MENU~~")
        try:
            menu = int(input("""1. Push
2. Pop
3. Peek (Top)
4. Display Stack
5. Check if Empty
6. Check if Full
0. Back to Main Menu\n>>> """))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if menu == 1:
            if len(pushed_ch) < 10:
                try:
                    push_message = int(input("Enter a value to push: "))
                    pushed_ch += [push_message]
                    print(pushed_ch)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            else:
                print("Overflow")
        elif menu == 2:
            if len(pushed_ch) > 0:
                popped_value = pushed_ch[-1]
                del pushed_ch[-1]
                print(f"Popped value: {popped_value}")
                print(pushed_ch)
            else:
                print("Underflow")
        elif menu == 3:
            if len(pushed_ch) > 0:
                print(pushed_ch[-1])
            else:
                print("Theres nothing to peek")
        elif menu == 4:
            print(pushed_ch)
        elif menu == 5:
            if len(pushed_ch) == 0:
                print("The list is Empty!")
            else:
                print(f"Its not Empty: You have {len(pushed_ch)}-elements in the list")
        elif menu == 6:
            if len(pushed_ch) == 10:
                print("The list is full")
            else:
                print(f"The list is not full: You have {len(pushed_ch)}-elements in the list")
        elif menu == 0:
            break
        else:
            print("Invalid choice! Please enter a number from 0 to 6.")

    # ============ QUEUE MENU (FIXED) ============
    while message == 2:
        print("~~QUEUE MENU~~")
        try:
            menu = int(input("""1. Enqueue
2. Dequeue
3. Peek (Front)
4. Display Queue
5. Check if Empty
6. Check if Full
0. Back to Main Menu\n>>> """))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if menu == 1:  # Enqueue at rear
            if len(pushed_ch) < 10:
                try:
                    enqueue_message = int(input("Enter a value to enqueue: "))
                    pushed_ch += [enqueue_message]
                    print(pushed_ch)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            else:
                print("Overflow")

        elif menu == 2:  # Dequeue from front
            if len(pushed_ch) > 0:
                dequeued_value = pushed_ch[0]
                # shift everything left manually using index tracking
                for i in range(len(pushed_ch) - 1):
                    pushed_ch[i] = pushed_ch[i + 1]
                del pushed_ch[-1]
                print(f"Dequeued value: {dequeued_value}")
                print(pushed_ch)
            else:
                print("Underflow")

        elif menu == 3:  # Peek front
            if len(pushed_ch) > 0:
                print(f"Front element: {pushed_ch[0]}")
            else:
                print("Theres nothing to peek")

        elif menu == 4:  # Display front to rear
            if len(pushed_ch) == 0:
                print("Queue is empty.")
            else:
                print("Front -> Rear:", pushed_ch)

        elif menu == 5:  # isEmpty
            if len(pushed_ch) == 0:
                print("The queue is Empty!")
            else:
                print(f"Its not Empty: You have {len(pushed_ch)}-elements in the queue")

        elif menu == 6:  # isFull
            if len(pushed_ch) == 10:
                print("The queue is full")
            else:
                print(f"The queue is not full: You have {len(pushed_ch)}-elements in the queue")

        elif menu == 0:
            break
        else:
            print("Invalid choice! Please enter a number from 0 to 6.")
    # ============ END QUEUE MENU ============

    if message == 0:
        active = False