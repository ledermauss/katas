
class KarateChopRecursive:

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def chop(self, target, array):
        # fuente de errores
        self.array = array
        self.target = target
        if (self.array_is_empty()):
            return -1
        begin = 0
        end = len(array) - 1
        return self.chop_recursive(begin, end)

    def array_is_empty(self):
        return len(self.array) == 0
    
    def chop_recursive(self, begin, end):
        if (self.split_is_singleton(begin, end)):
            return self.get_matching_index_or_error(begin)
        return self.find_split_and_chop(begin, end)


    def split_is_singleton(self, begin, end):
        return begin == end
    
    def get_matching_index_or_error(self, index):
        if (self.array[index] == self.target):
            return index
        else:
            return -1

    def find_split_and_chop(self, begin, end):
        left_split_end = self.get_end_of_left_split(begin, end)
        if (self.target_in_left_split(left_split_end)):
            # chop left
            return self.chop_recursive(begin, left_split_end)
        else:
            # chop right
            return self.chop_recursive(left_split_end + 1, end)
        

    def target_in_left_split(self, split_end):
        return self.target <= self.array[split_end]
     
    def get_end_of_left_split(self, begin, end):
        if (begin == end):
            return begin
        # if uneven, first list is larger
        return (begin + end) // 2


