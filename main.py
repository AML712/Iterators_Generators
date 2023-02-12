import types

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

class FlatIterator:
	def __init__(self, list_of_lists):
		self.list_of_lists = list_of_lists


	def __iter__(self):
		self.list_of_lists_iterator = iter(self.list_of_lists)
		self.list_of_lists_1 = []
		self.cursor = -1
		return self

	def __next__(self):
		self.cursor += 1
		if len(self.list_of_lists_1) == self.cursor:
			self.list_of_lists_1 = None
			self.cursor = 0
			while not self.list_of_lists_1:
				self.list_of_lists_1 = next(self.list_of_lists_iterator)
		return self.list_of_lists_1[self.cursor]


def flat_generator(list_of_lists):
	for item in list_of_lists:
		for element in item:
			yield element


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


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
	for item in FlatIterator(list_of_lists_1):
		print(item)

	print('\n')

	for item in flat_generator(list_of_lists_1):
		print(item)

	test_1()
	test_2()