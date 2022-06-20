from name_function import get_formatted_name

print("Enter 'q' any time to quit.")
while True:
    first = input("\nPlease give me your first name: ")
    if first.lower() == "q":
        break

    last = input("\nPlease give me your last name: ")
    if last.lower() == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")
