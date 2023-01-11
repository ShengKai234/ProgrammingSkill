import re

class Solution(object):
    def detectCaptial(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)

if __name__ == '__main__':
    print("template")
    solution = Solution()
    
    print("OutPut: ", solution.detectCaptial("word"), ", Shouls be True");
    print("OutPut: ", solution.detectCaptial("Google"), ", Shouls be True");
    print("OutPut: ", solution.detectCaptial("USA"), ", Shouls be True");
    print("OutPut: ", solution.detectCaptial("GoogLe"),", Shouls be False");

    print(re.fullmatch(r"[A-Z]*", "A"))
    print(re.fullmatch(r"[A-Z]*", "aaaa"))
    print(re.fullmatch(r"[A-Z]*", "AaaA"))
    print(re.fullmatch(r"[A−Z][a−z]*", "Aaaa"))
# T:O(n)
# S:O(n)