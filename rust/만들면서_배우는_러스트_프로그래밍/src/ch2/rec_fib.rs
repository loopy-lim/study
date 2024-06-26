fn fib(n: i64) -> i64 {
    if n == 1 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

fn main() {
    for i in 2..=20 {
        print!("{} ", fib(i));
    }
}
