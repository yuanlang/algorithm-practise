// 225. �ö���ʵ��ջ
// ʹ�ö���ʵ��ջ�����в�����

// push(x) -- Ԫ�� x ��ջ
// pop() -- �Ƴ�ջ��Ԫ��
// top() -- ��ȡջ��Ԫ��
// empty() -- ����ջ�Ƿ�Ϊ��
// ע��:

// ��ֻ��ʹ�ö��еĻ�������-- Ҳ���� push to back, peek/pop from front, size, �� is empty ��Щ�����ǺϷ��ġ�
// ����ʹ�õ�����Ҳ��֧�ֶ��С� �����ʹ�� list ���� deque��˫�˶��У���ģ��һ������ , ֻҪ�Ǳ�׼�Ķ��в������ɡ�
// ����Լ������в���������Ч�ģ�����, ��һ���յ�ջ������� pop ���� top ��������

import java.util.Deque;
import java.util.LinkedList;

class MyStack {
    Deque<Integer> q  = new LinkedList<>(); 

    /** Initialize your data structure here. */
    public MyStack() {
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        q.addFirst(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return q.removeFirst();
    }
    
    /** Get the top element. */
    public int top() {
        return q.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return this.q.size() == 0;
    }

    public static void main(String[] args) {

        // Your MyStack object will be instantiated and called as such:
        MyStack obj = new MyStack();
        obj.push(1);
        obj.push(2);
        int param_2 = obj.pop();
        System.out.println(param_2);
        int param_3 = obj.top();
        System.out.println(param_3);
        boolean param_4 = obj.empty();
        System.out.println(param_4);

    }

}
