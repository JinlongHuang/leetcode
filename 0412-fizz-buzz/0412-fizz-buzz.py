class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""] * n
    
        for i in range(n):
            if (i + 1) % 3 == 0:
                res[i] += "Fizz"
            if (i + 1) % 5 == 0:
                res[i] += "Buzz"
            if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
                res[i] += str(i+1)
                
        return res