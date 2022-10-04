class Box<T> {

    private T t;
    
    public void add(T t) {
     this.t=t;
    }
    
    public T get(){
     return t;
    }
    
    public static void main(String[] args) {
     Box<Integer> intBox = new Box<Integer>();
     
     
     intBox.add(10);
     System.out.println("output: " + intBox.get());
    }
}