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
    public void reorderList(ListNode head) {
        ListNode slow_pointer = head;
        ListNode fast_pointer = head;

        ListNode previous_node = null;
        ListNode current_node = null;
        ListNode next_node = null;

        ListNode list1_node = head;
        ListNode list2_node = null;
        int i = 0;

        while (fast_pointer.next != null && fast_pointer.next.next != null) {
            slow_pointer = slow_pointer.next;
            fast_pointer = fast_pointer.next.next;
        }
        current_node = slow_pointer.next;
        slow_pointer.next = null;

        while (current_node != null) {
            next_node = current_node.next;
            current_node.next = previous_node;
            previous_node = current_node;
            current_node = next_node;
        }
        list2_node = previous_node;
        current_node = null;

        while (list1_node != null || list2_node != null) {
            previous_node = current_node;
            if (i % 2 == 0) {
                current_node = list1_node;
                list1_node = list1_node.next;
            }
            else {
                current_node = list2_node;
                list2_node = list2_node.next;
            }
            if (previous_node != null) {
                previous_node.next = current_node;
            }
            i++;
        }
    }
}
