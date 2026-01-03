import os


def main():
    log_file_path = input("Enter log file path: ").strip()

    if not os.path.isfile(log_file_path):
        print("File not found in the specified path")
        return

    total_logs = 0
    log_level_counts = {}
    error_message_counts = {}

    with open(log_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                timestamp, level, message = line.split(" - ", 2)
            except ValueError:
                continue

            total_logs += 1

            if level in log_level_counts:
                log_level_counts[level] += 1
            else:
                log_level_counts[level] = 1

           
            if level == "ERROR":
                if message in error_message_counts:
                    error_message_counts[message] += 1
                else:
                    error_message_counts[message] = 1


    def get_count(item):
        return item[1]

    error_list = list(error_message_counts.items())

    error_list.sort(key=get_count, reverse=True)

    top_3_errors = error_list[:3]

    print("\n----- LOG SUMMARY -----")
    print(f"Total log entries: {total_logs}\n")

    print("Log Level Counts:")
    for level in log_level_counts:
        print(f"{level}: {log_level_counts[level]}")

    print("\nTop 3 Most Common ERROR Messages:")

    if not top_3_errors:
        print("No ERROR messages found.")
    else:
        i = 1
        for message, count in top_3_errors:
            print(str(i) + ". " + message + " (" + str(count) + " times)")
            i += 1

    main()
