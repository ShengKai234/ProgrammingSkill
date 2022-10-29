import java.util.List;

import javax.crypto.interfaces.PBEKey;

import java.util.ArrayList;

public class MyHashMap {
    private final int MAX_LEN = 10000;
    private List<int[]>[] map;

    private int getIndex(int key) {
        return key % MAX_LEN;
    }

    private int getPos(int key, int index) {
        List<int[]> tmp = map[index];
        if (tmp == null) {
            return -1;
        }

        for (int i = 0; i < tmp.size(); i++) {
            if (tmp.get(i)[0] == key) {
                return i;
            }
        }
        return -1;
    }

    /* init */
    public MyHashMap() {
        map = (List<int[]>[]) new ArrayList[MAX_LEN];
    }

    public void put(int key, int value) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos < 0) {
            if (map[index] == null) {
                map[index] = new ArrayList<int[]>();
            }
            map[index].add(new int[] {key, value});
        } else {
            map[index].set(pos, new int[] {key, value});
        }
    }

    public void remove(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            map[index].remove(pos);
        }
    }

    public int get(int key) {
        int index = getIndex(key);
        int pos = getPos(key, index);
        if (pos >= 0) {
            return map[index].get(pos)[1];
        }
        return -1;
    }

    public static void main(String []args) {
        System.out.println("My hash map!!");
        MyHashMap obj = new MyHashMap();
        int key = 299;
        int value = 2999999;
        obj.put(key,value);
        System.out.println(obj.get(key));
    }

    
}
