```
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
```

solution
========
```python
def detect_loop(lst):
    one_step = lst.get_head()
    two_step = lst.get_head()

    while one_step and two_step and two_step.next_element:
        one_step = one_step.next_element
        two_step = two_step.next_element.next_element

        if one_step == two_step:
            return True
    return False
```
