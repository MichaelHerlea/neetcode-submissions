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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode previous_node = dummy;
        ListNode current_node = head;
        int i = 0;

        while (current_node != null) {
            current_node = current_node.next;
            i++;
        }
        current_node = head;

        for (int j = 0; j < i - n; j++) {
            previous_node = current_node;
            current_node = current_node.next;
        }
        previous_node.next = current_node.next;

        return dummy.next;
    }
}
