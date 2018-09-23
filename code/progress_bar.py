

import sys
def loadingBar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + '  [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')




# Example: Double loop
# total = len(list1) * len(list2)
# count = 0 # how many have we done so far
# for i in range(len(list1)):
#   for j in range(len(list2)):
#       loadingBar(count,total,2)
#       count += 1
#       // DO PROCESSING OF [i,j]
