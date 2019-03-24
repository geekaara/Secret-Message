import os
import random
def prank_encrypt():
    file_list = os.listdir(r'C:\Users\Appalo family\Desktop\alphabet')
    saved_path = os.getcwd()
    os.chdir(r'C:\Users\Appalo family\Desktop\alphabet')
    for filename in file_list:
        a = random.randint(9,100)
        newname = ''.join((str(a),filename))
        os.rename(filename, newname)
    os.chdir(saved_path)
prank_encrypt()
