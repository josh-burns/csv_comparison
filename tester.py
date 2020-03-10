import filecmp
import sys
import difflib
from pprint import pprint
import fileinput

sample = sys.argv[-1]
control = sys.argv[-2]

# checks if txt files are the same
if filecmp.cmp(sample, control, shallow=False ):
    print("The values in the files match")
    sys.exit(0)

else:
    print("oh no! "+sample+" and "+control+" don't match. Give me a second, I will find which lines \n ...")

    def turnFiletoString(data):
        with open(data, 'r') as file:
            string= file.read() + '\n'
        return string.strip().splitlines()

    sampleString=turnFiletoString(sample)
    controlString=turnFiletoString(control)

    # displays diff line by line
    for line in difflib.unified_diff(sampleString, controlString, lineterm='', n=0):
        print(line)
    print("\n \nSee above differences between "+sample+" and "+control)
    sys.exit(1)
