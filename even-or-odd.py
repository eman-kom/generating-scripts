"""
I know there are better ways to check if a number is even or odd. But thats not the point of this script.
I just want to try generating scripts from another script.
"""

from argparse import ArgumentParser

def ifStmt(fileObj, minNum, maxNum):
    for num in range(minNum, maxNum+1):
        isStart = "if" if num == minNum else "elif"
        fileObj.write(f"{isStart} num == {num}:\n")
        fileObj.write(f"    print(f'{num} is {isEven(num)}.')\n")

    fileObj.write(f"else:\n")
    fileObj.write("    print(f'Sorry, I do not know if {num} is EVEN or ODD.')\n")


def dictSearch(fileObj, minNum, maxNum):
    fileObj.write("thisdict = {\n")
    for num in range(minNum, maxNum+1):
        fileObj.write(f"    {num} : '{isEven(num)}',\n")
    
    fileObj.write("}\n\n")
    fileObj.write("notFound = 'not found'\n")
    fileObj.write("print(f'{num} is {thisdict.get(num, notFound)}.')\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("minNum")
    parser.add_argument("maxNum")
    parser.add_argument("-i", "--ifStmt", action="store_true")
    args = parser.parse_args()

    isEven = lambda num : "EVEN" if num % 2 == 0 else "ODD"

    if args.filepath[-3:] != ".py":
        args.filepath += ".py"

    with open(args.filepath, "w") as fileObj:
        fileObj.write("from argparse import ArgumentParser\n\n")
        fileObj.write("parser = ArgumentParser()\n")
        fileObj.write("parser.add_argument('num')\n")
        fileObj.write("args = parser.parse_args()\n")
        fileObj.write("num = int(args.num)\n\n")

        if args.ifStmt:
            ifStmt(fileObj, int(args.minNum), int(args.maxNum))
        else:
            dictSearch(fileObj, int(args.minNum), int(args.maxNum))
