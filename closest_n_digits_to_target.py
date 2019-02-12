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

    top_n_list = []

    print(f"\nLooking for closest {closest_n_numbers} numbers in the given list to {target}.\nProcessing list...")

    for number in list_of_numbers:
        input_number_distance_from_target = abs(number - target)

        if not top_n_list:
            # print("List is empty")
            top_n_list.append(number)

        else:
            index_d = 0
            while index_d <= len(top_n_list) - 1:
                # While we are still within the bounds of the list
                current_number_in_top_n = top_n_list[index_d]
                current_number_in_top_n_distance_to_target = abs(current_number_in_top_n - target)

                if input_number_distance_from_target <= current_number_in_top_n_distance_to_target:
                    # Current input number is closer to the target than the current number in the top n list.
                    top_n_list.insert(index_d, number)
                    break
                elif index_d < len(top_n_list) - 1:
                    # advance to next number in top n list to compare the distances
                    index_d += 1
                    continue
                elif index_d == len(top_n_list)-1:
                    # index has reached the end of the list. Append the current value being checked to the end of the list
                    top_n_list.append(number)
                    break

    while len(top_n_list) > closest_n_numbers:
        top_n_list.pop()

    print("Processing done!")
    return top_n_list


if __name__ == "__main__":
    list_of_numbers = [13, 2, 29, 6, 11, 17, 8, 9, 10, 16]
    target =11
    closest_n_numbers = 6
    result = closest_n_digits_to_target(list_of_numbers, target, closest_n_numbers)
    msg = f"\nThe closest {closest_n_numbers} numbers  to {target} are {result}"
    print(msg)
