from IterGen import MyList, flat_generator
from Decorators import logger


@logger(log_path='iter_gen.log')
def iteration_generation(iterable):
    for i in iterable:
        print(i)


if __name__ == '__main__':
    nested_list = [1,
                   ['a', 'b', 'c'],
                   ['d', ['e', 'f'], 'h', False],
                   [1, 2, None]
                   ]

    iteration_generation(MyList(nested_list))
    iteration_generation(flat_generator(nested_list))
