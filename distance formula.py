
def blocks1(n):
	total = 0
	for row in range(1, n+1):
		total = total + row
	return(total)

def blocks2(n):
    if (n==1):
        return(1)
    else:
        return(blocks2(n-1) + n)
def blocks3(n):
    total = 0
    for row in range(1, n+1):
        for block in range(row, n+1):
            total = total +1
    return(total)
def blocks4(n):
    total = n*(n+1)/2
    return(total)

print(blocks1(-1), blocks2(1),blocks3(-1),blocks4(-1))
