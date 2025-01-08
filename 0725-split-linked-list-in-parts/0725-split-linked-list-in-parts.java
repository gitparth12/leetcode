import java.lang.*;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int distribution[] = new int[k];
        ListNode output[] = new ListNode[k];
        int listLength = 0;
        ListNode currentNode = head;
        while(currentNode != null) { // Calculates the length of the list
            listLength++;
            currentNode = currentNode.next;
        }
        currentNode = head;

        ListNode temp = head;
        if(listLength <= k) { // just populate the array with single elements
            int i = 0;
            while(currentNode != null) {
                output[i] = currentNode;
                temp = currentNode;
                currentNode = currentNode.next;
                temp.next = null;
                i++;
            }
        }
        else {
            boolean even = false;
            int max;
            if(listLength % k == 0) {
                even = true;
                max = listLength/k;
            }
            else
                max = ((int)listLength/k) + 1;
            
            for(int i = 0; i < output.length; i++) {
                output[i] = currentNode;
                for(int j = 0; j < max; j++) {
                    if(currentNode.next == null)
                        break;
                    temp = currentNode;
                    currentNode = currentNode.next;
                }
                if(i < output.length - 1)
                    temp.next = null;
                if(!even) {
                    if(i+1 == listLength % k) {
                        max--;
                        even = true;
                    }
                }
            }
        }
        return output;
    }
}