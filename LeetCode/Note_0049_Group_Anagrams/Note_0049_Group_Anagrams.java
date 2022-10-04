import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.omg.PortableInterceptor.SUCCESSFUL;

class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List> hash = new HashMap<>();

        for (String s: strs) {
            char[] c = s.toCharArray();
            Arrays.sort(c);
            
            String key = String.valueOf(c);
            System.out.println(key);

            if (!hash.containsKey(key)) {
                hash.put(key, new ArrayList());
            }
            hash.get(key).add(s);
        }
        System.out.println(hash);
        
        return new ArrayList(hash.values());
    }

    public List<List<String>> groupAnagrams_count(String[] strs) {
        int[] count = new int[26];
        Map<String, List> hash = new HashMap<>();
        for (String s: strs) {
            Arrays.fill(count, 0);
            for (char c: s.toCharArray()) {
                count[c - 'a']++;
            }

            StringBuilder sb = new StringBuilder("");
            for (int i = 0; i < count.length; i++) {
                sb.append(count[i]);
                sb.append("#");
            }

            String key = sb.toString();
            if (!hash.containsKey(key)) {
                hash.put(key, new ArrayList<>());
            }
            hash.get(key).add(s);
            System.out.println(hash.toString());
        }

        return new ArrayList(hash.values());
    }


    public static void main(String[] arg) {
        Solution solution = new Solution();
        List<List<String>> result = solution.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"});
        List<List<String>> result_count = solution.groupAnagrams_count(new String[]{"eat","tea","tan","ate","nat","bat"});
        System.out.println(result);
        System.out.println(result_count);
    }

}