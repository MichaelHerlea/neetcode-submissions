class MedianFinder {
    private final PriorityQueue<Integer> smallerHeap = new PriorityQueue<>(Collections.reverseOrder());
    private final PriorityQueue<Integer> largerHeap = new PriorityQueue<>();

    public MedianFinder() {
    
    }
    
    public void addNum(int num) {
        smallerHeap.add(num);
        largerHeap.add(smallerHeap.remove());
        if (smallerHeap.size() > largerHeap.size() + 1) largerHeap.add(smallerHeap.remove());
        if (smallerHeap.size() + 1 < largerHeap.size()) smallerHeap.add(largerHeap.remove());
    }
    
    
    public double findMedian() {
        if (smallerHeap.size() == largerHeap.size()) {
            return (smallerHeap.peek() + (double) largerHeap.peek()) / 2.0;
        } else {
            return largerHeap.peek();
    }
}
}
