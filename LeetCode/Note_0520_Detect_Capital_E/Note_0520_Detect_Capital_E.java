

public class Note_0520_Detect_Capital_E {

    // public Note_0520_Detect_Capital_E() {

    // }

    public boolean detectCapital(String word) {

        return word.matches("[A-Z]*|.[a-z]*");
    }

    public static void main(String []args) {
        System.out.println("Detect Capital!"); 
        Note_0520_Detect_Capital_E solution = new Note_0520_Detect_Capital_E();
        System.out.println("OutPut: " + solution.detectCapital("word") + ", Shouls be True");
        System.out.println("OutPut: " + solution.detectCapital("Google") + ", Shouls be True");
        System.out.println("OutPut: " + solution.detectCapital("USA") + ", Shouls be True");
        System.out.println("OutPut: " + solution.detectCapital("GoogLe") + ", Shouls be False");
    }
}