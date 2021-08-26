import random
import string
import sys
import time

def genpw():
    ans=''.join(random.choice(string.digits)for _ in range(4))
    #print (ans)
    return ans


def check(guess,ans,counter):
    ls_guess = list(str(guess))
    ls_ans = list(str(ans))
    cows=0
    bulls=0
    #print(ls_guess)
    #print(ls_ans)
    for i in range(4):
        if ls_guess[i] == ls_ans[i]:
           cows+=1
           ls_ans[i] = 'x'
           #print(ls_ans)


    for i in ls_guess:
        if i in ls_ans:
            bulls+=1
            ls_ans[ls_ans.index(i)] = 'x'
            #print(ls_ans)
            continue





    print("Cows is {}, Bulls is {}".format(cows,bulls))
    wincheck(cows,ans,counter)
    return cows,bulls

def wincheck(cows,ans,counter):
    if cows == 4:
        print("You win, the ans is:{}".format(ans))
        print("You had try {} times.".format(counter))
        time.sleep(2)
        sys.exit()

def main():
    ans = genpw()
    counter=0
    while True:
        try:
            guess = input("input a 4 numbers int:")
            if len(guess) != 4:
                print("Need 4 Numbers")
                continue
            if isinstance(guess,int) :
                print("Need Numbers")
                continue
        except Exception as e:
            print ("some error")

        counter +=1
        cows,bulls = check(guess,ans,counter)

if __name__ == "__main__":
    main()
