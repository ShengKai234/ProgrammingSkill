import java.util.List;
import java.util.ArrayList;

class MyHashSet {
    private final int MAX_LEN = 10000;
    private List<Integer>[] set;

    /* Return corresponding bucket index. */
    private int getIndex(int key) {
        return key % MAX_LEN;
    }

    private int getPos(int key, int index) {
        // Each bucket contain a list
        List<Integer> temp = set[index];
        if (temp == null) {
            return -1;
        }

        // Iterate all the elements in the bucket to find the target key.
        for (int i = 0; i < temp.size(); i++) {
            if (temp.get(i) == key) {
                return i;
            }   
        }
        return -1;
    }

    /* init */
    public MyHashSet() {
        set = (List<Integer>[]) new ArrayList[MAX_LEN];
    }

    public void add(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            // Add new key if key does not exit
            if (set[index] == null) {
                set[index] = new ArrayList<Integer>();
            }
            set[index].add(key);
        }
    }

    public void remove(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            // Remove the key if key exists.
            set[index].remove(pos);
        }
    }

    /** Returns true if this set did already contain the specified element */
    public boolean contains(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        return pos >= 0;
    }

    public static void main(String []arg) {
        System.out.println("My hash set!!");
        int key = 299;
        MyHashSet obj = new MyHashSet();
        obj.add(key);
        System.out.println("key: " + key + ", " + obj.contains(key));
        obj.remove(key);
        System.out.println("key: " + key + ", " + obj.contains(key));
        
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */