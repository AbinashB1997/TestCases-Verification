import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/user_input.in/')
from app1 import demo_class as x

x = x()


def count_correctNess():
    file1 = open('../approach2/input.in/in1.txt', "r")
    inputF = file1.readlines()

    file1.close()

    file3 = open('../approach2/user_output.in/out1.txt', 'a')
    for testCases in range(len(inputF)):
        l = []
        s = inputF[testCases][1 : ]
        for i in s:
            if(i.isnumeric()):
                l.append(int(i))
        file3.write(str(x.countOnes(l, len(l))))
        file3.write('\n')

    file3.close()
    cnt = 0

    with open('../approach2/user_output.in/out1.txt', "r") as f1, open('../approach2/output.in/out1.txt', 'r') as f2:
        for l1, l2 in zip(f1, f2):
            if l1 == l2:
                cnt += 1
    print (cnt)

count_correctNess()