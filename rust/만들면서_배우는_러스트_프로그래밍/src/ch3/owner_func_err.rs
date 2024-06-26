fn main() {
    let g1 = String::from("실수 할 줄 아는 사람이 알음답다");
    show_message(g1);
    println!("{}", g1);
}

fn show_message(msg: String) {
    println!("{}", msg);
}
