/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var swapPairs = function(head) {
    let result = new ListNode(-1);
    result.next = head;
    let tmp = result;
    while(tmp.next != null && tmp.next.next != null)
    {
        let cur = tmp.next;
        let Next = tmp.next.next;
        tmp.next = Next;
        cur.next = Next.next;
        Next.next = cur;

        tmp = cur;
    }

    return result.next
};

// 因为是值引用，所以要定义出一个多余节点来找到转换后的结果
// 头指针的多次交换