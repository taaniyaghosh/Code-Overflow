public class quickUnionUF {
    private int[] id;

    // set id of each element to itself
    public quickUnionUF(int N) {
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    //find the root of the element
    private int root(int i) {
        while (id[i] != i)
            i = id[i];
        return i;
    }

    // check if p and q are connected
    public boolean connected(int p, int q) {
        return (root(p) == root(q));
    }

    //perform union of 2 elements
    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }

    // perform weighted quick union
    public void wQuickUnion(int p, int q) {
        int i = root(p);
        int j = root(q);
        if(i==j)
            return;
        else if{

        }
    }
}
