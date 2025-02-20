import sys

def insertion_sort():
    for i in range(1, len(input_list)):
        element = input_list[i]
        j = i-1
        while j >= 0 and element.lower() < input_list[j].lower():
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = element
    return input_list

input_list = sys.argv[1:]
print('User given strings are: \n', input_list)

sorted_list = insertion_sort()
print('Sorted strings are: \n', sorted_list)
