
class KarateChop:

    def chop(self, target, array):
        begin = 0
        end = len(array)
        while begin != end:
            mid = self.get_end_of_first_split(begin, end) 
            if (array[mid] == target):
                return mid
            elif (target > array[mid]):
                begin = mid + 1
            elif (target < array[mid]):
                end = mid
            # optimization if target not in array of len > 1
            else: 
                return -1
        return -1

    def get_end_of_first_split(self, begin, end):
        # if uneven, first list is larger
        if (begin == end):
            return begin
        return (begin + end) // 2

