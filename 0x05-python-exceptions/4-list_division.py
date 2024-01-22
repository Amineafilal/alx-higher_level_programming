#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_res = []

    for d in range(list_length):
        try:
            result = my_list_1[d] / my_list_2[d]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            list_res.append(result)
    return (list_res)
