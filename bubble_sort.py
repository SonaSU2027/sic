import sys
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-2):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
def bubble_sort(array):
    for i in range(len(array)-1):
        swap=True
        for j in range(len(array)-2):
            if array[j]>array[j+1]:
                swap=False
                array[j],array[j+1]=array[j+1],array[j]
        if sorted:
            return

input_list = sys.argv[1:]
print('User given strings are: \n', input_list)

sorted_list = bubble_sort()
print('Sorted strings are: \n', sorted_list)