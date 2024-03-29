package Algorithms.Graph;

class UnionFind {
    private int[] rootArray;

    public UnionFind(int size) {
        rootArray = new int[size];
        for (int i = 0; i < size; i++) {
            rootArray[i] = i;
        }
    }

    public int find(int v) {
        return rootArray[v];
    }

    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            for (int i = 0; i < rootArray.length; i++) {
                if (rootArray[i] == rootY) {
                    rootArray[i] = rootX;
                }
            }
        }
    }
    
    public boolean connected(int x, int y) {
        return find(x) == find(y);
    }
}

public class QuickFind {
    public static void main(String[] args) throws Exception {
        UnionFind uf = new UnionFind(10);
        // 1-2-5-6-7 3-8-9 4
        uf.union(1, 2);
        uf.union(2, 5);
        uf.union(5, 6);
        uf.union(6, 7);
        uf.union(3, 8);
        uf.union(8, 9);
        System.out.println(uf.connected(1, 5)); // true
        System.out.println(uf.connected(5, 7)); // true
        System.out.println(uf.connected(4, 9)); // false
        // 1-2-5-6-7 3-8-9-4
        uf.union(9, 4);
        System.out.println(uf.connected(4, 9)); // true
    }
}