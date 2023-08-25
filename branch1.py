class Process:
    def _init_(self, process_id, name, start_time, priority):
        self.process_id = process_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def _str_(self):
        return f"{self.process_id}\t{self.name}\t{self.start_time}\t{self.priority}"

processes = [
    Process("P11", "VSCode", 100, "MID"),
    Process("P23", "Eclipse", 234, "MID"),
    Process("P42", "Chrome", 189, "High"),
    Process("P87", "JDK", 9, "High"),
    Process("Process", "CMD", 7, "High"),
    Process("VSCode", "NotePad", 23, "Low")
]

while True:
    print("\nMenu:")
    print("1. Sort by Process ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        processes.sort(key=lambda x: x.process_id)
        print("Process ID\tName\tStart Time\tPriority")
        print("---------------------------------------")
        for process in processes:
            print(process)
    elif choice == '2':
        processes.sort(key=lambda x: x.start_time)
        print("Process ID\tName\tStart Time\tPriority")
        print("---------------------------------------")
        for process in processes:
            print(process)
    elif choice == '3':
        processes.sort(key=lambda x: x.priority, reverse=True)
        print("Process ID\tName\tStart Time\tPriority")
        print("---------------------------------------")
        for process in processes:
            print(process)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        
        
#github link :- https://github.com/samriddhi-018/Lab_03-Assignment/tree/main