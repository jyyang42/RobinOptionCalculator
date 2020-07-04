import math


def get_d1(p0, X, t, sigma, Rho):
    # P0 stock price 62
    # X exercise Price 60
    # t time to expiration days/365  40
    # sigma Volatility  0.32
    # Rho Risk-Free Rate  0.04

    # d1 = {ln(62/60) + [0.04 + 0.5 * 0.32 ^ 2] * (40/365)} / 0.32 * sqrt(40/365)
    a = math.log(p0/X) + (Rho + 0.5 *  sigma * sigma) * (t / 365)
    b = sigma * math.sqrt(40/365)
    return a/b
    
def get_d2(d1, sigma, t):
    # d1 - sigma * sqrt(t/365)
    return d1 - sigma * math.sqrt(t/365)

def get_cumulative_standard_normal_distribution(d):
    return 0.5 * (1 + math.erf(d/math.sqrt(2)))

def get_call(p0, Nd1, X, Krf, t, Nd2):
    a = p0 * Nd1
    b = X / (math.pow(math.e, Krf * t/365))
    return a - b * Nd2

def get_put(Vc, X, Krf, t, p0):
    return Vc + X / math.pow(math.e, Krf * t/365) - p0
    

if __name__ == "__main__":
    # Z = (x - µ) / sigma
    p0 = 62
    X = 60
    t = 40
    sigma = 0.32
    Rho = 0.04

    d1 = get_d1(p0, X, t, sigma, Rho)
    d2 = get_d2(d1, sigma, t)
    Nd1 = get_cumulative_standard_normal_distribution(d1)
    Nd2 = get_cumulative_standard_normal_distribution(d2)
    Vc = get_call(p0, Nd1, X, Rho, t, Nd2)
    Vp = get_put(Vc, X, Rho, t, p0)

    print("d1:", d1)
    print("d2:", d2)
    print("Nd1:", Nd1)
    print("Nd2:", Nd2)
    print("Vc:", Vc)
    print("Vp:", Vp)