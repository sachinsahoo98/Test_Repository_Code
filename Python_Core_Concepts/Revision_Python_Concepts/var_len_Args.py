
def varLengthArgs(*args, **kwargs):

    """
    :param args: takes variable length of positional arguements
    :param kwargs: takes variable length of keyword arguements
    :return: None
    """
    print("Positional Arguements are:")
    print(args)
    for arguement in args:
        print(arguement)
    print("Keyword Arguements are:")
    print(kwargs)
    for key, value in kwargs.items():
        print("Key:", key, "Value:", value)

varLengthArgs("Sachin", 26, "Barang", gender="M", jobStatus="Unemployed")