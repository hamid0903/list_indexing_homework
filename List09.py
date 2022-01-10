def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    return  list1[0]==list1[1] and list1[1]==list1[2] and list1[2]==list1[3] and list1[3]==list1[4]
print(main([1,1,2,2,3]))