import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Arrays;


public class JavaHeap {
    
    public static void main(String []args) {

        System.out.println("-----1. init-----");
        // O(N)
        // 
        // Construct an empty Min Heap
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // Construct an empty Max Heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        // Construct a Heap with initial elements.
        // This is named "Heapify"
        // The Heap is a Min Heap
        PriorityQueue<Integer> heapWithValues = new PriorityQueue<>(Arrays.asList(3, 1, 2));
        PriorityQueue<Integer> maxHeapWithValues = new PriorityQueue<>(Arrays.asList(3, 1, 2));

        
        System.out.println("minHeap: " + minHeap);
        System.out.println("maxHeap: " + maxHeap);
        System.out.println("heapWithValues: " + heapWithValues);

        System.out.println("-----2. insert-----");
        // Insert an element to the Min Heap
        minHeap.add(5);
        minHeap.add(6);

        // Insert an element to the Max Heap
        maxHeap.add(5);
        maxHeap.add(6);

        // Insert an element to heapWithValues(Min Heap)
        heapWithValues.add(0);
        System.out.println("minHeap: " + minHeap);
        System.out.println("maxHeap: " + maxHeap);
        System.out.println("heapWithValues: " + heapWithValues);

        System.out.println("-----3. peek-----");

        // Get top element from the Min Heap
        // i.e. the smallest element
        System.out.println("Minimum value from minHeap: " + minHeap.peek());

        // Get top element from the Max Heap
        // i.e. the smallest element
        System.out.println("Maximum value from maxHeap: " + maxHeap.peek());

        System.out.println("Minimum value from heapWithValues(Min Heap): " + heapWithValues.peek());

        System.out.println("-----4. pop (poll)-----");

        // Delete top element from the Min Heap
        System.out.println("Delete Minimum value from minHeap: " + minHeap.poll());

        // Delete top element from the Max Heap
        System.out.println("Delete Maximum value from maxHeap: " + maxHeap.poll());

        // Delete top element from the heapWithValues(Min Heap)
        System.out.println("Delete Maximum value from maxHeap: " + heapWithValues.poll());

        System.out.println("-----5. size / isEmpty-----");
        // Length of the Min Heap
        System.out.println("Length of the Min Heap: " + minHeap.size());

        // Length of the Max Heap
        System.out.println("Length of the Max Heap: " + maxHeap.size());

        // Length of the heapWithValues
        System.out.println("Length of the heapWithValues(Min Heap): " + heapWithValues.size());
    }
}



