# Normal iteration
def cal_Collatz_sequence1(start, end):
    print("Number\tSteps")

    # 1. Which number between 1 and 100 takes the most steps to reach 1
    num1 = 0
    most_step = 0

    # 2. What is the highest number reached across all 100 sequences
    highest_num = 0

    # 3. Which numbers take exactly the same number of steps to reach 1 as the number itself.
    numbers = []

    for i in range(start, end + 1):
        cur_step = 0  # Initial value to count
        cur_num = i  # 2. Save the current initial value

        # Loop until number reach 1
        while i != 1:
            # 2. Check to find the highest number
            if i > highest_num:
                highest_num = i

            # If even number
            if i % 2 == 0:
                i /= 2

            # Odd number
            else:
                i = 3 * i + 1

            # Count step
            cur_step += 1

        # 1. Check to find the largest steps
        if cur_step > most_step:
            num1 = cur_num
            most_step = cur_step

        # 3. Compare number with its steps
        if cur_step == cur_num:
            numbers.append(cur_num)

        # print("{0:>6}".format(cur_num), "{0:>6}".format(cur_step))

    # Result for 1.
    print("\t------")
    print(f"Number '{num1}' takes the most steps ({most_step} steps) to reach 1.")

    # Result for 2.
    print("\t------")
    print(f"The highest number reached across all 100 sequences is: {int(highest_num)}")

    # Result for 3.
    print("\t------")
    print("The numbers take exactly the same number of steps to reach 1 as the number itself:", end=" ")

    for num in numbers:
        print(num, end="  ")


def cal_Collatz_sequence2(start, end):
    res_list = {}

    print("Number\tSteps")

    # 1. Which number between 1 and 100 takes the most steps to reach 1
    num1 = 0
    most_step = 0

    # 2. What is the highest number reached across all 100 sequences
    highest_num = 0

    # 3. Which numbers take exactly the same number of steps to reach 1 as the number itself.
    numbers = []

    for i in range(start, end + 1):
        cur_step = 0  # Initial value to count
        cur_num = i  # 2. Save the current initial value

        # Loop until number reach 1
        while i != 1:
            # 2. Check to find the highest number
            if i > highest_num:
                highest_num = i

            if i in res_list:
                cur_step += res_list[i]
                break

            # If even number
            if i % 2 == 0:
                i /= 2

            # Odd number
            else:
                i = 3 * i + 1

            # Count step
            cur_step += 1

        res_list[cur_num] = cur_step

        # 1. Check to find the largest steps
        if cur_step > most_step:
            num1 = cur_num
            most_step = cur_step

        # 3. Compare number with its steps
        if cur_step == cur_num:
            numbers.append(cur_num)

        # print("{0:>6}".format(cur_num), "{0:>6}".format(cur_step))

    # Result for 1.
    print("\t------")
    print(f"Number '{num1}' takes the most steps ({most_step} steps) to reach 1.")

    # Result for 2.
    print("\t------")
    print(f"The highest number reached across all 100 sequences is: {int(highest_num)}")

    # Result for 3.
    print("\t------")
    print("The numbers take exactly the same number of steps to reach 1 as the number itself:", end=" ")

    for num in numbers:
        print(num, end="  ")


def cal_Collatz_sequence3(start, end):
    # Create empty list to store results
    result_list = {}

    # Calculate the results for the largest number
    dynamic_Collatz(end, result_list)

    print("Number\tSteps")

    # 1. Which number takes the most steps to reach 1
    num1 = 0
    most_step = 0

    # 3. Which numbers take exactly the same number of steps to reach 1 as the number itself.
    numbers = []

    for i in range(start, end + 1):
        # If the number hasn't been calculated
        if i not in result_list:
            dynamic_Collatz(i, result_list)

        # Get the number of steps of the current number
        cur_step = result_list[i]

        # 1. Check to find the largest steps
        if cur_step > most_step:
            num1 = i
            most_step = cur_step

        # 3. Compare number with its steps
        if cur_step == i:
            numbers.append(i)

        # print("{0:>6}".format(cur_num), "{0:>6}".format(res[cur_num - start]))

    # Result for 1.
    print("\t------")
    print(f"Number '{num1}' takes the most steps ({most_step} steps) to reach 1.")

    # 2. What is the highest number reached across all sequences
    print("\t------")
    highest_num = max(result_list.keys())
    print(f"The highest number reached across all 100 sequences is: {int(highest_num)}")

    # Result for 3.
    print("\t------")
    print("The numbers take exactly the same number of steps to reach 1 as the number itself:", end=" ")

    for num in numbers:
        print(num, end="  ")


# Recursively solve from the input number and all of its sub-problems then store result in res-list
def dynamic_Collatz(num, res_list):
    if num in res_list:
        return res_list[num]

    if num == 1:
        res_list[num] = 0

    # Number is even
    elif num % 2 == 0:
        res_list[num] = 1 + dynamic_Collatz(int(num / 2), res_list)

    # Number is even odd
    else:
        res_list[num] = 1 + dynamic_Collatz(3 * num + 1, res_list)

    return res_list[num]


if __name__ == '__main__':
    cal_Collatz_sequence1(1, 10 ** 7)
