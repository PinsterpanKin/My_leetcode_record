"""
The original solution is a clear description of the conversion process, 
but it is a bit too long. 
We can use a more concise way to achieve the same result.
"""

class Solution(object):
    def intToRoman(self, num):
        result=""
        while num>=1000:
            num-=1000
            result+="M"
        if num>=900:
            num-=900
            result+="C"
            result+="M"
        if num>=500:
            num-=500
            result+="D"
        if num>=400:
            num-=400
            result+="C"
            result+="D"
        while num>=100:
            num-=100
            result+="C"
        if num>=90:
            num-=90
            result+="X"
            result+="C"
        if num>=50:
            num-=50
            result+="L"
        if num>=40:
            num-=40
            result+="X"
            result+="L"
        while num>=10:
            num-=10
            result+="X"
        if num>=9:
            num-=9
            result+="I"
            result+="X"
        if num>=5:
            num-=5
            result+="V"
        if num>=4:
            num-=4
            result+="I"
            result+="V"
        while num>=1:
            num-=1
            result+="I"
        return result

"""A more concise way to achieve the same result."""

class Solution(object):
    def intToRoman(self, num):
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        result=""
        for i in range(len(values)):
            while num>=values[i]:
                num-=values[i]
                result+=symbols[i]
        return result