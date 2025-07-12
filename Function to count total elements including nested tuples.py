def count_all_element(input_a_tuple):
    total_ind_elm = 0
    breakdown = []

    for item in input_a_tuple:
        if isinstance(item, tuple):
            for elm in item:
                total_ind_elm = total_ind_elm + 1
            breakdown.append(len(item))
    
        elif type(item) is int:
            total_ind_elm = total_ind_elm + 1
            breakdown.append(1)
    

    convert_list_to_str = ' + '.join(str(e) for e in breakdown)


    print(f"Output: {total_ind_elm} ({convert_list_to_str})")
    
count_all_element((1, (2, 3), 4, (5, 6, 7)))
count_all_element(((1, 2, 3)))
count_all_element((1, (2, 3), 4))
count_all_element((5, (6,), 7, 8))
count_all_element(((1, 2, 3), 4, 5))
count_all_element((1, (2, (3, 4)), 5))
count_all_element(((1,), (2, 3), (4, 5, 6)))
count_all_element((1, 2, (3, 4), (5, (6, 7))))
count_all_element(((), 1, (2, 3), ()))
count_all_element((((),),))
count_all_element((1, (2, (3, (4, (5,))))))






