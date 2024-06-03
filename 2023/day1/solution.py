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

    converted_string = ''

    # for each index in eightwothree
    for i in range(len(string)):
        # if number, just add
        if string[i].isdigit():
            converted_string += string[i]
            continue
        # else, not number, it's letter -> check using dict
        else:
            j = i
            while j <= len(string):
                if string[i:j] in digit_letter_dict.keys():
                    converted_string += digit_letter_dict[string[i:j]]
                    break
                else:
                    j += 1
    
    return converted_string


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