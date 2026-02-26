import os

filename = "markanalyser.txt"
student_list = []
marks_list = []
while True:
    print("Menu:")
    print("1. Enter student marks")
    print("2. View all marks")
    print("3. Search for a student's mark")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0

        students = int(input("Enter how many students: "))
        for i in range(students):
            name = input(f"Enter name for student {i+1}: ")
            mark = float(input(f"Enter mark for {name}: "))
            student_list.append(name)
            marks_list.append(mark)

        with open(filename, "a") as file:
            if write_header:
                file.write("Student Name\tMark\n")
            for name, mark in zip(student_list, marks_list):
                file.write(f"{name}\t{mark}\n")

        if marks_list:
            highest_mark = max(marks_list)
            lowest_mark = min(marks_list)
            average_mark = sum(marks_list) / len(marks_list)
            students_above_75 = sum(1 for mark in marks_list if mark > 75)
            print(f"Highest Mark: {highest_mark}")
            print(f"Lowest Mark: {lowest_mark}")
            print(f"Average Mark: {average_mark:.2f}")
            print("Students with marks above 75:", students_above_75)
        else:
            print("No marks entered.")

    elif choice == '2':
        try:
            with open(filename, "r") as file:
                content = file.read()
                if content.strip():
                    print("Student Marks:")
                    print(content)
                else:
                    print("No marks recorded yet.")
        except FileNotFoundError:
            print("No marks recorded yet.")

    elif choice == '3':
        search = input("Enter a student name to retrieve their mark (or press Enter to skip): ").strip()
        if search:
            found = False
            if student_list and marks_list:
                for name, mark in zip(student_list, marks_list):
                    if name.lower() == search.lower():
                        print(f"{name}'s mark: {mark}")
                        found = True
                        break
            if not found:
                try:
                    with open(filename, "r") as file:
                        lines = file.readlines()
                        if len(lines) > 1:
                            for line in lines[1:]:
                                parts = line.strip().split("\t")
                                if len(parts) == 2 and parts[0].lower() == search.lower():
                                    print(f"{parts[0]}'s mark: {parts[1]}")
                                    found = True
                                    break
                except FileNotFoundError:
                    print("No marks recorded yet.")
            if not found:
                print(f"No mark found for student: {search}")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break