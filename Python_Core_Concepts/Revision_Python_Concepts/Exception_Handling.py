def testFunction(num):
    """

    :param num: Takes any number
    :return:None
    """
    try:
        result = num/0
    except Exception as e:
        print("Errors generated as runtime is:", e)
    else:
        print("Result after divison is:", result)
    finally:
        print("executing rest of code")

testFunction(5)
