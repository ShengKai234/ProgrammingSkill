package MultiThreads;
public class Threads {

    public static void main(String []arg) throws InterruptedException {
        final Thread sepeThread = new Thread(new ThreadPrinter());
        sepeThread.start();
        for (int i = 0; i < 5; i++) {
            System.out.println("From the main thread "
                + Thread.currentThread().getName());
            Thread.sleep(1000);
        }
    } 
}