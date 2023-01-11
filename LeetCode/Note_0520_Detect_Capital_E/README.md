# Detect Capital
## Solution 1:
    

## Solution 2:
    使用Regex
- case 1: 使用 "[A-Z]*"，確認第一個字元為A-Z，出現 0次或多次
    - "*" 代表: 出現 0次或多次(全部都是)
- case 2: 使用 ".[a-z]*"，確認第一個字元為a-z，出現 0次或多次
    - "." 代表: any character
- combine: [A-Z]*|.[a-z]*
    - "|" 代表: 或 / orå