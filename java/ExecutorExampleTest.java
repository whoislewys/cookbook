import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
Run this with:
javac ExecutorExampleTest.java && java ExecutorExampleTest
*/

public class ExecutorExampleTest {
  public static void main(String[] args) {
    ExecutorExample ex = new ExecutorExample();
    ex.run();
  }
}

class ExecutorExample {
  private final ExecutorService pool;
  private int threadNum;

  public ExecutorExample() {
    this.pool = Executors.newFixedThreadPool(2);
    this.threadNum = 0;
  }

  public void run() {
    try {
      pool.execute(new Handler(threadNum));
      threadNum++;
      pool.execute(new Handler(threadNum));
    }
    catch(Exception e) {
      System.out.println("exception");
      pool.shutdown();
    }
  }
}

class Handler implements Runnable {
  private int threadNum;

  public Handler(int threadNum) {
    this.threadNum = threadNum;
  }

  public void run() {
    while(true) {
      System.out.println("Thread num:");
      System.out.println(this.threadNum);
      try {
        Thread.sleep(2000);
      }
      catch(Exception E) {}
    }
  }
}
