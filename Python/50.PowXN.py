class MySolution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if not n:
                return x
            else:
                return fastPow(x*x, n-1)
        
        if not n:
            return float(1)
        res = 1
        negative = (n < 0)
        n = abs(n)
        remain = n
        current_pow = 0
        while n > current_pow:
            power, depth = 1, 0
            while remain >= power<<1:
                power <<= 1
                depth += 1
            remain -= power
            current_pow += power
            res *= fastPow(x, depth)
        return float(1/res) if negative else res