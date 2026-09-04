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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        ListNode l1 = null;
        ListNode l2 = null;
        while (lists.length > 1) {
            List<ListNode> temp_list = new ArrayList<>();
            for (int i = 0; i < lists.length; i+=2) {
                l1 = lists[i];
                if (i + 1 < lists.length) {
                    l2 = lists[i + 1];
                }
                else {
                    l2 = null;
                }
                temp_list.add(mergeLists(l1, l2));
            }
            lists = temp_list.toArray(new ListNode[0]);
        }
        return lists[0];
    }

    public ListNode mergeLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode head_node = null;
        if (l1.val < l2.val) {
            head_node = l1;
            l1 = l1.next;
        }
        else {
            head_node = l2;
            l2 = l2.next;
        }
        ListNode current_node = head_node;

        while (!(l1 == null && l2 == null)) {
            if (l1 == null) {
                current_node.next = l2;
                break;
            }
            if (l2 == null) {
                current_node.next = l1;
                break;
            }

            if (l1.val < l2.val) {
                current_node.next = l1;
                l1 = l1.next;
            }
            else {
                current_node.next = l2;
                l2 = l2.next;
            }
            current_node = current_node.next;;
        }

        return head_node;
    }
}
