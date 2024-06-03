import re

# part 2
digit_letter_dict = {
            "one": "1",
            "two": '2',
            "three": '3',
            "four": '4',
            "five": '5',
            "six": '6',
            "seven": '7',
            "eight": '8',
            "nine": '9'
            }

def convert_letter_to_num(string):

    # for each index in eightwothree
    for i in range(len(string)):
        # for each index, start slicing the window +1 until len(string)
        j = i
        # slicing window until len(string)
        while j <= len(string):
            # if the window matches, replace the window with the number from dict, and
            # recursivly call on that newly changed string
            if string[i:j] in digit_letter_dict.keys():
                string = string.replace(string[i:j], digit_letter_dict[string[i:j]])
                convert_letter_to_num(string)
            # no match: keep on +1 the window slicing
            else:
                j += 1
        
    # If no changes are made in this iteration, return the result
    return string


def sum_calibrations(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        lines = [i.strip() for i in lines]

    sum_calibrations = 0
    
    for line in lines:
        line = convert_letter_to_num(line)
        digits_list = re.findall("\d+", line)                   # i.e. ["12", "34"]
        digits_string = "".join(digits_list)                    # i.e. "1234"
        calibration = digits_string[0] + digits_string[-1]      # i.e."14"
        sum_calibrations += int(calibration)

    return sum_calibrations



input = "2023/day1/input.txt"
print(sum_calibrations(input))