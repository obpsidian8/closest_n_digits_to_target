def closest_n_digits_to_target(list_of_numbers, target, closest_n_numbers):
    """
    Function that takes in a list of numbers and returns the closest n digits to that target. "n" is the third parameter of the function
    :param list_of_numbers:
    :param target:
    :param closest_n_numbers:
    :return: closest n digits to target
    """

    if closest_n_numbers > len(list_of_numbers):
        print("Closest n digits must be less than list given")
        return

    top_three_list = []

    print(f"\nLooking for closest {closest_n_numbers} numbers in the given list to {target}.\nProcessing list...")

    for number in list_of_numbers:
        input_number_distance_from_target = abs(number - target)

        if not top_three_list:
            # print("List is empty")
            top_three_list.append(number)

        else:
            # print("Checking list contents")
            for digit in top_three_list:
                top_three_number_distance_to_target = abs(digit - target)
                index_d = top_three_list.index(digit)
                if input_number_distance_from_target <= top_three_number_distance_to_target:
                    # print(f"Current number is closer to target then digit")

                    top_three_list.insert(index_d, number)
                    if len(top_three_list) > closest_n_numbers:
                        top_three_list.pop()
                    break

                else:
                    if index_d < len(top_three_list)-1:
                        continue

                    elif index_d == len(top_three_list)-1 and len(top_three_list) < closest_n_numbers :
                        top_three_list.append(number)
                        break
                    else:

                        continue


    while len(top_three_list)>closest_n_numbers:
        top_three_list.pop()

    print("Processing done!")
    return top_three_list


if __name__ == "__main__":
    list_of_numbers = [13, 2, 29, 6, 11, 17, 8, 9, 10, 16]
    target = 10
    closest_n_numbers = 6
    result = closest_n_digits_to_target(list_of_numbers, target, closest_n_numbers)
    msg = f"\nThe closest {closest_n_numbers} numbers  to {target} are {result}"
    print(msg)
