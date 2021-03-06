from Decorators import logger


class MyList:

    def __init__(self, my_list: list):
        self.my_list = my_list
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.my_list):
            self.cursor += 1
            if not isinstance(self.my_list[self.cursor - 1], list):
                return self.my_list[self.cursor - 1]
            else:
                self.my_list = list(self.my_list[self.cursor - 1]) + self.my_list[self.cursor:]
                self.cursor = 0
                return self.__next__()
        else:
            raise StopIteration


def flat_generator(some_list):
    for list_item in some_list:
        if not isinstance(list_item, list):
            yield list_item
        else:
            yield from flat_generator(list_item)


