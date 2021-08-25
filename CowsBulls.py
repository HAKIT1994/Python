import random
import string
import sys
import time

def genpw():
    ans=''.join(random.choice(string.digits)for _ in range(4))
   # print (ans)
    return ans


def check(guess,ans,counter):
    ls_guess = list(str(guess))
    ls_ans = list(str(ans))
    cows=0
    bulls=0
    for i in range(4):
        if ls_guess[i] == ls_ans[i]:
           cows+=1
           ls_ans[i] = 10

        else:
            for j in range(4):
                if i==j: break
                if ls_guess[i] == ls_ans[j]:
                   bulls+=1
                   ls_ans[j] = 10
                   break

                #print(ls_ans)


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
