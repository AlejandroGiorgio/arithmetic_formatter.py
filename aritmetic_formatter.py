
def aritmetic_formatter(numlist, decider):
    formatedList = []
    firstColumn = ""
    secondColumn = ""
    lines = ""
    resolve = ""
    printLine = ""
    if len(numlist) > 4:
        return (print("Error: Too many problems."))
    else:
        pass

    for count in numlist:
        formated = count.split(" ")
        try:
            num1 = int(formated[0])
            num2 = int(formated[2])
            operator = formated[1]
            if len(formated[0]) < 5 and len(formated[2]) < 5:
                if operator == "+" or operator == "-":
                    # Here it catchs when the operator is not "+" or "-"
                    formatedList.append(formated)
                else:
                    print("Error: Operator must be '+' or '-'.")
                    break
            # Here ir catchs when the numbers are more than 4 digits
            else:
                print("Error: Numbers cannot be more than four digits.")
                break
        # Here the error is catched when the values are not digits and the error count sums 1
        except ValueError:
            print("Error: Numbers must only contain digits.")
            break

    for a in formatedList:
        num1 = a[0]
        num2 = a[2]
        op = a[1]
        lenght = max(len(num1), len(num2)) + 2

        if op == "+":
            res = str(int(num1)+int(num2))
        else:
            res = str(int(num1)-int(num2))

        first = str(num1).rjust(lenght)
        second = op + str(num2).rjust(lenght - 1)
        line = ""
        result = res.rjust(lenght)
        for x in range(lenght):
            line += "-"

        if a != formatedList[-1]:
            firstColumn += first+"    "
            secondColumn += second+"    "
            lines += line + "    "
            resolve += result + "    "
        else:
            firstColumn += first
            secondColumn += second
            lines += line
            resolve += result

    if decider is True:
        printLine = firstColumn + "\n" + secondColumn + "\n" + lines + "\n" + resolve
        print(printLine)
    else:
        printLine = firstColumn + "\n" + secondColumn + "\n" + lines
        print(printLine)


aritmetic_formatter(["2 + 22", "1 + 3", "3333 + 2222", "44 * 3444"], True)
