class Solution(object):
    def intToRoman(self, num: int) -> str:

        def transferToRoman(digi: int, ten: int, five: int, one: int):
            res = ''
            if digi >= 10:
                for i in range(digi // 10):
                    res += ten
            elif digi >= 9:
                res += one + ten
            elif digi >= 5:
                res += five
                for i in range(digi - 5):
                    res += one
            elif digi >= 4:
                res += one + five
            else:
                for i in range(digi):
                    res += one
            return res

        res = ""
        
        res += transferToRoman(num//1000, '', '', 'M')

        num %= 1000
        res += transferToRoman(num//100, 'M', 'D', 'C')

        num %= 100
        res += transferToRoman(num//10, 'C', 'L', 'X')

        num %= 10
        res += transferToRoman(num, 'X', 'V', 'I')

        return res
        


            # if num >= 1000:
            #     num -= 1000
            #     res += 'M'
            # elif num >= 900:
            #     num -= 900
            #     res += 'CM'
            # elif num >= 500:
            #     num -= 500
            #     res += 'D'
            # elif num >= 400:
            #     num -= 400
            #     res += 'CD'
            # elif num >= 100:
            #     num -= 100
            #     res += 'C'
            # elif num >= 90:
            #     num -= 90
            #     res += 'XC'
            # elif num >= 50:
            #     num -= 50
            #     res += 'L'
            # elif num >= 40:
            #     num -= 40
            #     res += 'XL'
            # elif num >= 10:
            #     num -= 10
            #     res += 'X'
            # elif num >= 9:
            #     num -= 9
            #     res += 'IX'
            # elif num >= 5:
            #     num -= 5
            #     res += 'V'
            # elif num >= 4:
            #     num -= 5
            #     res += 'IV'
            # else:
            #     num -= 1
            #     res += 'I'
        # return res
   

if __name__ == '__main__':
    print("template")
    solution = Solution()
    print(solution.intToRoman(1994))

# T:O(n)
# S:O(n)