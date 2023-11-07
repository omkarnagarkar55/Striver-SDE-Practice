class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        n = len(s)
        # Creating a dictionary for Roman Symbols
        Symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        i=0

        # Calculating the integer value from Roman. The loop is upto 2nd last element
        while(i < n-1):
            # Performing subtraction (bet. val of next - val of cur) when when one of the six condition are met.
            if s[i] == "I" and s[i+1] in ["V","X"] or s[i] == "X" and s[i+1] in ["L","C"] or s[i] =="C" and s[i+1] in ["D","M"]:
                value += Symbols[s[i+1]] - Symbols[s[i]]
                i+=1 
            else:
                # Adding all the values     
                value += Symbols[s[i]]
            print(value)
            i+=1
        
        # Adding the last number to the value if any last number is remaining
        if i < n:
            value += Symbols[s[i]]
        return value
        