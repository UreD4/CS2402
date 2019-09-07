from timeit import default_timer as timer 
import sys

with open('test.txt', 'r') as file:
    data = file.read()

strSet=data.split('\n')
strList=list(strSet)


    

def reCall(list,stuff):
    if len(list)==0:
        return 0
    elif len(stuff[0])!=len(list[0]):
        return 0+reCall(list[1:],stuff)
    elif stuff[1]==list[0]:
        return 0+reCall(list[1:],stuff)
    elif stuff[0]==sorted(list[0]):
        stuff[2].append(list[0])
        return 1+reCall(list[1:],stuff)
    else:
        return 0+reCall(list[1:],stuff)

def main():
    isDone=True
    
    while isDone:
        if sys.version_info[0] >2:
            comparie = input('Enter a word or empty string to finish:  ')
        elif sys.version_info[0]<3:
            comparie = raw_input('Enter a word or empty string to finish:  ')#my workstation is using python 2.7 for now
        if not comparie:
            print('Bye, thanks for using the program!')
            sys.exit(0)
        str1 = sorted(comparie)
        anaSet =[]
        stuffToPass=[str1,comparie,anaSet]
        start = timer()
        count =reCall(strList,stuffToPass)
        print('The word %s has %s anagrams:' % (comparie,count))
        for i in range(0,len(anaSet)):
            print(anaSet[i])
        end = timer()  
        timeTotal = end - start
        print('it took a total of %s seconds to find the anagrams'%(timeTotal))

main()
