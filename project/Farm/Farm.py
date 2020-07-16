#leg and head solve
#totleg = chicken*2 + pig *4
#tothead = chicken +pig
def solve(head,totleg):
    for chicken in range(1,head+1):
        pig=head-chicken
        if leg==4*pig+2*chicken:
            return pig,chicken
    return None,None

head=int(input('head ?='))
leg= int(input('leg?='))
pig ,chicken =solve(head,leg)
if pig==None and chicken == None:
    print('no solution')
else:
    print('pig=',pig)
    print('chicken=',chicken)
