def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    num=list_num[0]
    if list_num[1]>=num:
        num=list_num[1]
    if list_num[2]>=num:
        num=list_num[2]
    if list_num[3]>=num:
        num=list_num[3]
    if list_num[4]>=num:
        num=list_num[4]

    return num
print(main([12,5,30,4,8]))