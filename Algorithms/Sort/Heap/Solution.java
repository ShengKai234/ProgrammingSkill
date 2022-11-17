import java.util.Arrays;

/**
 * HeapSort
 */
public class Solution {

    public void heapSort(int[] arr) {
        for (int i = arr.length / 2 - 1; i >= 0; i--) {
            maxHeapify(arr, arr.length, i);
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
            maxHeapify(arr, i, 0);
        }

        System.out.println(Arrays.toString(arr));
    }

    public void maxHeapify(int[] arr, int heap_size, int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int large = index;
        if (left < heap_size && arr[left] > arr[large]) {
            large = left;
        }
        if (right < heap_size && arr[right] > arr[large]) {
            large = right;
        }
        if (large != index) {
            int tmp = arr[index];
            arr[index] = arr[large];
            arr[large] = tmp;
            
            // if swap, we have to check child node
            maxHeapify(arr, heap_size, large);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] lst = {7,3,2,5,6,10,9,8,1};
        System.out.print(Arrays.toString(lst) + " sorted to ");
        solution.heapSort(lst);
    }
}