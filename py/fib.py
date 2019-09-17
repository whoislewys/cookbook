class fibonacci():
    def nextFib(self, n):
        if n == 0:
            return 0;
        if n == 1:
            return 1;
        return self.nextFib(n - 1) + self.nextFib(n - 2)

    def memoizedNextFib(self, n, cache):
        if n == 0:
            return 0;
        if n == 1:
            return 1;

        if n not in cache:
            leftRec = self.memoizedNextFib(n - 1, cache)
            rightRec = self.memoizedNextFib(n - 2, cache)
            cache[n] = leftRec + rightRec
            return leftRec + rightRec
        else:
            return cache[n]


if __name__ == '__main__':
    fibonacci = fibonacci()

    print(fibonacci.nextFib(4))
    print(fibonacci.memoizedNextFib(4, {}))
