import random
def largePrime_Generate(bit=1024):
    # print("Generating large prime......")
    i=1
    while(True):
        num=random.randrange(2**(bit-1),2**(bit))
        # print("{}th randmon num is:{}.".format(i,num))
        if(isPrime(num)):
            # print("{} is probably prime".format(num))
            return num
        else:
            i+=1
def isPrime(testNum=1000000000063):
    smallPrime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,233,239,
                241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,
                421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,
                607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,
                809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
    if(testNum<2):
        return False
    if testNum in smallPrime:
        return True
    for prime in smallPrime:
        if(testNum%prime==0):
            return False
    return(Miller_Rabin(testNum))
def Miller_Rabin(testNum=1000000000061):
    safeTime=10
    eulerN=testNum-1
    oddQ=0
    testNum2=0
    while(eulerN%2==0):
        testNum2=testNum2+1
        eulerN=eulerN//2
    oddQ=eulerN
    for trials in range(safeTime):
        random_a=random.randrange(2,testNum-1)
        firstTest=pow(random_a,oddQ,testNum)
        if(firstTest==1 or firstTest==testNum-1):
            continue
        else:
            nextTest=firstTest
            for i in range(1,testNum2):
                nextTest=(nextTest**2)%testNum
                if(nextTest==testNum-1):
                    break
            return False
    return True
def generateLargePrime_basedOnMR(bit):
    while(True):
        try:
            bit=eval(input())
            largePrime_Generate(bit)
            break
        except:
            print("error")
if __name__=="__main__":
    generateLargePrime_basedOnMR(1000)