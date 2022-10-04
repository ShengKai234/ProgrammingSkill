import java.lang.reflect.Method;

class Reflection {

    private Integer t;
    
    public void add(Integer t) {
        this.t=t;
    }
    
    public Integer get(){
        return t;
    }
    
    public static void main(String[] args) throws ClassNotFoundException {
        Class rect = Class.forName("Reflection");

        Method[] f_methods = rect.getDeclaredMethods();
        for(Method f_method : f_methods){
            //get the name of the method
            System.out.println("Method Name: " + f_method.getName());
        }
    }
}