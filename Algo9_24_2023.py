#Write a function to return a new list where all None values are replaced with the most recent non-None value in the list.



def fill_none(input_list):
    prev_value = 0

    result = []
    for value in values:
        if value is None:
            result.append(prev_value)
        else:
            result.append(value)
            prev_value = value
    return result