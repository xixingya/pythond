a=[];
i=0;
sum=0;
while i<10 :
    a.append(int(input()))
    sum=sum+a[i]
    i=i+1
a.sort()
print(a[0])
print(sum/10)


