
class ArrayHelper:
    @staticmethod
    def is_even_len(array):
        return len(array) % 2 == 0
    @staticmethod
    def is_empty(array):
        return len(array) == 0

    @staticmethod
    def is_singleton(array):
        return len(array) == 1

    @staticmethod
    def match_target(target, array, split_index):
        if target == array[0]:
            return split_index
        return -1

    @staticmethod
    def contains_target(target, array):
        return  array[0]<= target and array[-1] >= target

    @staticmethod
    def split(array, split_index):
        left_split = array[:split_index+1]
        right_split = array[split_index+1::]
        return left_split, right_split

    @staticmethod
    def get_end_of_first_split(array):
        return (len(array) - 1) // 2

        


class KarateChopSlices:
    @staticmethod
    def chop(target, array):
        if (ArrayHelper.is_empty(array)):
                return -1
        chopped_array = array
        global_index = ArrayHelper.get_end_of_first_split(array)
        next_index = global_index
        while not ArrayHelper.is_singleton(chopped_array):
            left_split, right_split = ArrayHelper.split(chopped_array, next_index)
            if ArrayHelper.contains_target(target, left_split):
                chopped_array = left_split
                next_index = ArrayHelper.get_end_of_first_split(chopped_array)
                global_index = update_global_index_left(global_index, next_index, chopped_array)
            elif ArrayHelper.contains_target(target, right_split):
                chopped_array = right_split
                next_index = ArrayHelper.get_end_of_first_split(chopped_array)
                global_index = update_global_index_right(global_index, next_index)
            else:
                return -1
        return ArrayHelper.match_target(target, chopped_array, global_index)



def update_global_index_right(global_index, split_index):
    # first: [0, 1, 2, 3, 4, 5, 6 | 7, 8, 9, 10, 11, 12] - global = split = 6
    # right: [7, 8, 9 | 10, 11, 12] - split = 2, global = 9 (global + split + 1)
    # right: [10, 11 | 12] - (left) split = 1, global = 11 (global + split + 1)
    return split_index + global_index + 1

def update_global_index_left(global_index, split_index, current_array):
    if (ArrayHelper.is_even_len(current_array)):
        return global_index - split_index - 1
    else:
        return global_index - split_index

    # first: [0, 1, 2, 3, 4, 5, 6 | 7, 8, 9, 10, 11, 12] - global = split = 6
    # left:  [0, 1, 2, 3 | 4, 5, 6] - split = 3, global = 3 (global - split, uneven) 
    # left:  [0, 1 | 2, 3] - (left) split = 1, global = 1 (global - split - 1, even)
    
    




    



