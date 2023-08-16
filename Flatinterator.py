class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.item = []
        
    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
       self.item = [item for lot in self.list for item in lot]
       self.cursor +=1
       if self.cursor > (len(self.item)-1):
           raise StopIteration
       return self.item[self.cursor]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
        

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()