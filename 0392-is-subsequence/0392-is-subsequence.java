class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.equals(""))
            return true;

        int i = 0;
        char tArr[] = t.toCharArray();
        
        for(char c: t.toCharArray()) {
            if(c == s.charAt(i)) {
                i++;
            }
            if(i == s.length())
                return true;
        }
        return false;
    }
}