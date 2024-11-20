import math

def fact(x):
    if x < 0:
        factor =0
        return factor
    else:
        factor= math.factorial(int(x))
    return factor

def root(x):
    if x < 0:
        rooted=0
        return rooted
    else:
        rooted= math.sqrt(x)

    return rooted


def trunk(x):
    trunked = math.trunc(x)
    return trunked


def main():
    x=float(input("Please insert a number: "))
    f= fact(x)
    r=root(x)
    t=trunk(x)

    print("The factorial of ", x,"is : ",f, ".")
    print("The square root of ", x,"is : ",r, ".")
    print("The trunk of ", x,"is : ",t,".")

    
main()