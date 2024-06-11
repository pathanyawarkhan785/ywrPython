val1 = int(input("enter val1: "))

match val1:
    case 1:
        print("this is 1")
    case 2:
        print("this is 2")
    case _ if val1 < 20:
        print("val1 is lessthan 20.")
    case _ if val1 < 10:
        print(
            "val1 is lesser than 10."
        )  # here if val1 = 5 ,still this line not executed because upper line's condition satisfied.
        # so we need to write < 10 condition first to run this line.
    case _:
        print("this is default case.")
