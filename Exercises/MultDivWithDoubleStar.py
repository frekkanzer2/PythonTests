def myOperation(first, second, **operation):
    if operation.get("action") == "mult":
        print("Multiplication result:", first * second)
    elif operation.get("action") == "div":
        if first >= second:
            print("Division result:", first / second)
        else:
            print("Division result:", second / first)
    if operation.get("flag") == "watch":
        if operation.get("action") == "mult":
            print(first, "x", second)
        elif operation.get("action") == "div":
            if first >= second:
                print(first, ":", second)
            else:
                print(second, ":", first)
    elif operation.get("flag") == "noWatch":
        print("You can't see the operation")


myOperation(25, 5, action="div", flag="noWatch")
myOperation(4, 8, action="mult", flag="watch")
