def compute_average(): 
    numbers = input("Enter numbers separated by spaces: ").split()

    numbers = [float(num) for num in numbers]

    average = sum(numbers) / len(numbers)

    print(f"The average is {average: .2f}")

compute_average()
