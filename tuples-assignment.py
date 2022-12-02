"""Write a function called skip_tuples. It has a tuple as input. It returns a new tuple as output, such as every second element of the input tuple is skipped, starting with the first one.

Example:

The input tuple is('I', 'am', 'a', 'test', 'tuple')

This will return the tuple ('I', 'a', 'tuple').

Don’t forget to write a docstring for the above function.

Put your testcases in main()"""

tuple = ('I', 'am', 'a', 'test', 'tuple')


def skip_tuples(a):
    newTuple = ()
    for num in range(len(a)):
        print(num)
        if num % 2 == 0:
            newTuple += (a[num],)
    return newTuple


if __name__ == "__main__":
    print(skip_tuples(tuple))
