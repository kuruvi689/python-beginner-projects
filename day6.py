def collect_data():
    students = {}
    count = int(input("How many students do you want to enter? "))
    for i in range(count):
        name = input(f"Enter name of student {i+1}: ")
        mark = float(input(f"Enter mark for {name}: "))
        if name in students:
            choice = input(f"{name} already exists. Do you want to overwrite the mark? (yes/no): ").strip().lower()
            if choice == "yes":
                students[name] = mark
        else:
            students[name] = mark
    return students


def analyse_data(students):
    if not students:
        print("No student data to analyze.")
        return
    marks = list(students.values())
    highest_mark = max(marks)
    lowest_mark = min(marks)
    average_mark = sum(marks) / len(marks)
    above_75 = sum(1 for mark in marks if mark > 75)
    print(f"Highest Mark: {highest_mark}")
    print(f"Lowest Mark: {lowest_mark}")
    print(f"Average Mark: {average_mark:.2f}")
    print(f"Number of students with marks above 75: {above_75}")


def save_data(students, filename="reportcard.txt"):
    with open(filename, "a") as file:
        file.write("Student Name\tMark\n")
        for name, mark in students.items():
            file.write(f"{name}\t{mark}\n")


def search_student(students):
    search_name = input("Enter a student name to search for their mark: ").strip()
    if search_name in students:
        print(f"{search_name}'s mark: {students[search_name]}")
    else:
        print(f"{search_name} not found in the records.")


def main():
    students = {}
    while True:
        print("\nMenu:")
        print("1. Collect student data")
        print("2. Analyze data")
        print("3. Save data to file")
        print("4. Search for a student's mark")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            students = collect_data()
        elif choice == '2':
            analyse_data(students)
        elif choice == '3':
            save_data(students)
            print("Data saved to reportcard.txt")
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()