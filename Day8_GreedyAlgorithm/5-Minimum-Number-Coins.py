def MinimumCoins(n: int) -> List[int]:
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    coins = []
    for i in range(len(deno)-1,-1,-1):
        while(n>=deno[i]):
            n-=deno[i]
            coins.append(deno[i])
    return coins