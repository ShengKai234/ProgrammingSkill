class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] s1map = new int[26];
        int[] s2map = new int[26];

        // create s1, s2 char hashmap to 0 - 26
        for (int i = 0; i < s1.length(); i++) {
            s1map[s1.charAt(i) - 'a']++;
            s2map[s2.charAt(i) - 'a']++;
        }
        
        // siding window s2map (remove preceding character(s1map[s2[i] - 'a']) and add new succeding character(s1map[s2[i + s1.length()] - 'a']))
        // and compare all the elements of s2map for equality to get the required result(s1)
        for (int i = 0; i < s2.length() - s1.length(); i++) {
           if (match(s1, s1map, s2map)) return true;
            s2map[s2.charAt(i + s1.length()) - 'a']++;
            s2map[s2.charAt(i) - 'a']--;
        }

        // check last element left by for-loop
        return match(s1, s1map, s2map);
    }

    public boolean match(String s1, int[] s1map, int[] s2map) {
        for (int j = 0; j < s1.length(); j++) {
            if (s2map[s1.charAt(j) - 'a'] != s1map[s1.charAt(j) - 'a']) {
                return false;
            }
        }
        return true;
    }
}