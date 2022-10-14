import java.util.*;

class Solution {

    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> cmp = new Comparator<String>() {
            @Override
            public int compare(String log1, String log2) {
                String[] arr1 = log1.split(" ", 2);
                String[] arr2 = log2.split(" ", 2);
                
                boolean isDigit1 = Character.isDigit(arr1[1].charAt(0));
                boolean isDigit2 = Character.isDigit(arr2[1].charAt(0));

                if (!isDigit1 && !isDigit2) {
                    int cmpLetter = arr1[1].compareTo(arr2[1]);
                    if (cmpLetter == 0) {
                        return arr1[0].compareTo(arr2[0]);
                    }
                    return cmpLetter;
                }

                if (!isDigit1 && isDigit2) {
                    return -1;
                } else if (isDigit1 && !isDigit2) {
                    return 1;
                }
                return 0;
            }
        };

        Arrays.sort(logs, cmp);
        return logs;
    }

    public static void main(String[] args) {
        System.out.println("LeetCode 0937..."); 
        Solution solution = new Solution();
        String[] testCase = new String[] {"dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"};
        System.out.println("test case: " + Arrays.toString(testCase)); 
        String[] res = solution.reorderLogFiles(testCase);
        System.out.println("result: " + Arrays.toString(res)); 

    }
}