package MultiThreads;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public class UsingExecutor {
    public static void main(String[] arg) {
        final Executor executor = Executors.newCachedThreadPool();
        executor.execute(new ThreadPrinter());
        executor.execute(new ThreadPrinter());
        executor.execute(new ThreadPrinter());
    }
}