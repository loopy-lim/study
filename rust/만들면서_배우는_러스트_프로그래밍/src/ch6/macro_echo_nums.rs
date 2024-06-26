#[macro_export]
macro_rules! echo_nums {
  ($($num:expr), *) => {
    $(
      print!("{}, ", $num);
    )*
    println!("");
  }
}

fn main() {
    echo_nums!(10, 20, 30);
    echo_nums![40, 50, 60];
    echo_nums! {70, 80, 90};
}
