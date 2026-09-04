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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list1_node = list1;
        ListNode list2_node = list2;

        ListNode head_node = null;
        ListNode tail_node = null;

        // Checking for edge cases
        if (list1_node == null && list2_node == null) {
            return null;
        }
        else if (list1_node == null) {
            return list2_node;
        }
        else if (list2_node == null) {
            return list1_node;
        }

        // Setting the head of our new linked list
        if (list1_node.val <= list2_node.val) {
            head_node = list1_node;
            list1_node = list1_node.next;
        }
        else {
            head_node = list2_node;
            list2_node = list2_node.next;
        }
        tail_node = head_node;

        while (true) {
            if (list1_node == null) {
                tail_node.next = list2_node;
                break;
            }
            else if (list2_node == null) {
                tail_node.next = list1_node;
                break;
            }

            if (list1_node.val <= list2_node.val) {
                tail_node.next = list1_node;
                tail_node = list1_node;
                list1_node = list1_node.next;
            }
            else {
                tail_node.next = list2_node;
                tail_node = list2_node;
                list2_node = list2_node.next;
            }
        }

        return head_node;
    }
}