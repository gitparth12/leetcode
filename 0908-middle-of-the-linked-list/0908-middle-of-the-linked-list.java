import java.util.*;

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
    public ListNode middleNode(ListNode head) {
        List<ListNode> nodes = new ArrayList<ListNode>();
        ListNode current = head;
        while(current != null) {
            nodes.add(current);
            current = current.next;
        }
        return nodes.get((int)Math.ceil(nodes.size()/2));
    }
}