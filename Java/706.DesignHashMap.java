class MyHashMap {

        private static class Node {
            int key;
            int value;

            Node(int key, int value) {
                this.key = key;
                this.value = value;
            }
        }

        private static final int NUM_BUCKETS = 1009;
        private final List<LinkedList<Node>> buckets;

        public MyHashMap() {
            buckets = new ArrayList<>(NUM_BUCKETS);
            for (int i = 0; i < NUM_BUCKETS; i++) {
                buckets.add(new LinkedList<>());
            }
        }

        private int getHash(int key) {
            return Math.abs(key) % NUM_BUCKETS;
        }

        public void put(int key, int value) {
            int bucketIdx = getHash(key);
            LinkedList<Node> bucket = buckets.get(bucketIdx);

            for (Node node : bucket) {
                if (node.key == key) {
                    node.value = value; 
                    return;
                }
            }

            bucket.add(new Node(key, value));
        }

        public int get(int key) {
            int bucketIdx = getHash(key);
            LinkedList<Node> bucket = buckets.get(bucketIdx);

            for (Node node : bucket) {
                if (node.key == key) {
                    return node.value;
                }
            }

            return -1; 
        }

        public void remove(int key) {
            int bucketIdx = getHash(key);
            LinkedList<Node> bucket = buckets.get(bucketIdx);

            bucket.removeIf(node -> node.key == key);
        }
}