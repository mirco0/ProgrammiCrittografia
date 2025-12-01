from Gruppi import Group

def algo_pollard_rho(G: Group,n,alpha,beta):

    def procedure(x,a,b):
        if x in S1:
            f = ( (beta*x) % n, a, (b+1) % n)
        elif x in S2:
            f = ( (x*x) % n, 2*a % n, 2*b % n)
        else: 
            f = ( (a*x) % n, (a+1) % n, b)

    return f

    x,a,b = f(1,1,0)
    x_p,a_p,b_p = f(x,a,b)
    while x != x_p:
        x,a,b = f(x,a,b)
        x_p,a_p,b_p = f(x_p,a_p,b_p)
        x_p,a_p,b_p = f(x_p,a_p,b_p)
    
    if gcd() != 1:
        print("FAIL")
    else:
        return ( ((a - a_p) * G.exp(b_p-b,-1)) % n)


