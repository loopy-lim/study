macro_rules! map_init {
  ($($key:expr => $val:expr),*) => {{
    let mut tmp = std::collections::HashMap::new();
    $(
      tmp.insert($key, $val);
    )*
    tmp
  }}
}

fn main() {
    let weekdays = map_init! {
      "Monday" => 0,
      "Tuesday" => 1,
      "Wednesday" => 2,
      "Thursday" => 3,
      "Friday" => 4,
      "Saturday" => 5,
      "Sunday" => 6
    };

    for (day, num) in weekdays {
        println!("{}: {}", day, num);
    }
}
