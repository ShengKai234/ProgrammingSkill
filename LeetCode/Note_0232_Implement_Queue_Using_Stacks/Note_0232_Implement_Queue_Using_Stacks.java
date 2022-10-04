import java.util.*;

class MyQueue {

    private int front;
    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();

    public MyQueue() {
        
    }
    
    public void push(int x) {
        if (this.s1.isEmpty()) {
            this.front = x;
        }
        this.s1.push(x);
    }
    
    public int pop() {
        if (this.s2.isEmpty()) {
            while (!this.s1.isEmpty()) {
                this.s2.push(this.s1.pop());
            }
        }
        return this.s2.pop();
    }
    
    public int peek() {
        if (!this.s2.isEmpty()) {
            return this.s2.peek();
        }
        return this.front;
    }
    
    public boolean empty() {
        return this.s1.isEmpty() && this.s2.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        MyQueue myQueue = new MyQueue();
        myQueue.push(1);
        myQueue.push(2);
        System.out.println(myQueue.peek());
        System.out.println(myQueue.pop());
        System.out.println(myQueue.empty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */