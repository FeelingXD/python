# not solved.
customer=map(int,input().split())
customer=list(set(customer))
customer.append('$')
for i in customer :
    print(i ,end=' ')
