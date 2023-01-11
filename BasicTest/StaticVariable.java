import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.io.IOException;
import java.time.ZoneId;

public class StaticVariable {

    static int val;
    StaticVariable(int v) {
        this.val = v;
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        // StaticVariable classTest1 = new StaticVariable(1);
        // StaticVariable classTest2 = new StaticVariable(2);
        // StaticVariable classTest3 = new StaticVariable(3);
        // StaticVariable classTest4 = new StaticVariable(4);

        // System.out.println(classTest1.val); 
        // System.out.println(classTest2.val); 
        // System.out.println(classTest3.val); 
        // System.out.println(classTest4.val); 

        // String test = "123456";
        // String test1 = test;
        // test = "098765";

        // System.out.println(test); 
        // System.out.println(test1);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss'Z'");
        ZonedDateTime zonedDateTime = ZonedDateTime.now(ZoneId.of("UTC"));
        System.out.println(zonedDateTime.format(formatter));
    }
}
