def sort_012(input_list):
    next_index_0=0
    next_index_2=len(input_list)-1
    current_index=0
    while(current_index)<next_index_2+1:
        current_element=input_list[current_index]
        if current_element==0:
            input_list[current_index]=input_list[next_index_0]
            input_list[next_index_0]=current_element
            next_index_0=next_index_0+1
            current_index=current_index+1
        elif current_element==1:
            current_index=current_index+1+1
        elif current_element==2:
            input_list[current_index]=input_list[next_index_2]
            input_list[next_index_2]=current_element
            next_index_2=next_index_2-1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
