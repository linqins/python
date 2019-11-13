a=13.5
j=0
for i in range(0,100,5):
    
    sum = a*i/100;
    print("sum_%d: %.4f \t" %(j,sum),end="")
    j +=1
    if j%3 ==0 :
        print("")