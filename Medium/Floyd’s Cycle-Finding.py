def detect_loop(lst):
    one_step = lst.get_head()
    two_step = lst.get_head()

    while one_step and two_step and two_step.next_element:
        one_step = one_step.next_element
        two_step = two_step.next_element.next_element

        if one_step == two_step:
            return True
    return False
