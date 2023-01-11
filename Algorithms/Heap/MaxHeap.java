import java.text.NumberFormat.Style;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;

public class MaxHeap {

    private int heapSize, realSize;
    private int[] maxHeap;
    
    public MaxHeap(int size) {
        this.heapSize = size;
        this.realSize = 0;
        this.maxHeap = new int[this.heapSize];
    }

    private void add(int value) {
        this.realSize++;

        if (this.realSize > this.heapSize) {
            System.out.println("element is full !!");
            this.realSize--;
            return;
        }

        this.maxHeap[this.realSize] = value;
        
        int index = this.realSize;
        int parent = this.realSize / 2;

        while (parent > 0 && this.maxHeap[parent] < this.maxHeap[index]) {
            int tmp = this.maxHeap[index];
            this.maxHeap[index] = this.maxHeap[parent];
            this.maxHeap[parent] = tmp;
            index = parent;
            parent = index / 2;
        }
    }

    public Integer peek() {
        return this.maxHeap[1];
    }

    public Integer pop() {

        if (this.realSize < 1) {
            System.out.println("Don't have any element !!");
            return Integer.MAX_VALUE;
        } else {
            Integer pop_value = this.maxHeap[1];
            this.maxHeap[1] = this.maxHeap[this.realSize];
            this.maxHeap[this.realSize] = 0;
            this.realSize--;

            int index = 1;
            while (index <= this.realSize / 2) {
                int left_child = index * 2;
                int right_child = index * 2 + 1;

                if (this.maxHeap[left_child] > this.maxHeap[index] || this.maxHeap[right_child] > this.maxHeap[index]) {
                    if (this.maxHeap[left_child] > this.maxHeap[right_child]) {
                        int tmp = this.maxHeap[left_child];
                        this.maxHeap[left_child] = this.maxHeap[index];
                        this.maxHeap[index] = tmp;
                        index = left_child;
                    } else {
                        int tmp = this.maxHeap[right_child];
                        this.maxHeap[right_child] = this.maxHeap[index];
                        this.maxHeap[index] = tmp;
                        index = right_child;
                    }
                } else {
                    break;
                }
            }
            return pop_value;
        }
    }

    public int size() {
        return this.realSize;
    }

    public void print() {
        System.out.println("print ...");
        for (int i = 0; i < this.realSize; i++) {
            System.out.println(this.maxHeap[i]);
        }
    }

    public static void main(String []arg) {
        // MaxHeap maxHeap = new MaxHeap(10);

        // maxHeap.add(10);
        // maxHeap.add(200);
        // maxHeap.add(2000);
        // maxHeap.print();
        // maxHeap.add(100);
        // maxHeap.pop();
        // maxHeap.print();


        Map<String, String> bracketMap = new HashMap<>();
        bracketMap.put(")", "(");
        bracketMap.put("]", "[");
        bracketMap.put("}", "{");

        List<String> t = new ArrayList<>();

        String s = "(())";
        for (int i = 0; i < s.length(); i++) {
            if (bracketMap.containsKey(Character.toString(s.charAt(i)))) {
                if (t.get(t.size() - 1) != bracketMap.get(Character.toString(s.charAt(i)))) {
                    System.out.println("false");
                    // return false;
                } else {
                    t.remove(t.size() - 1);
                }
            } else {
                t.add(Character.toString(s.charAt(i)));
            }
        }
        System.out.println("true");
    }
}
