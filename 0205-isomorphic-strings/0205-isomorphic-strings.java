import java.util.*;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length())
            return false;
        char sList[] = s.toCharArray();
        char tList[] = t.toCharArray();
        HashMap<Character, Character> dict = new HashMap<Character, Character>();
        for(int i = 0; i < s.length(); i++) {
            if(dict.get(sList[i]) == null) {
                if(!dict.values().contains(tList[i]))
                    dict.put(sList[i], tList[i]);
                else
                    return false;
            }
            else if(dict.get(sList[i]) != tList[i])
                return false;
        }
        return true;
    }
}