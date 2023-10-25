from MarkovLibrary import *

if __name__ == '__main__':


    s=input("Введите правила\n")
    d=input("Введите слово\n")
    if check_rules(s,"#"):
        start(s,d)
    else:
        print("введите условие")

