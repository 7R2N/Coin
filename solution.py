def coins(coin1,coin2):
    if coin1 % 2 == 0 and coin2 % 2 == 0:
        return -1
    elif coin1 % coin2 == 0 or coin2 % coin1 == 0:
        return -1
    elif coin1 % 3 == 0 and coin2 % 3 == 0:
        return -1
    elif coin1 % 5 == 0 and coin2 % 5 == 0:
        return -1
    else:
        return (coin1-1)*(coin2-1)-1
