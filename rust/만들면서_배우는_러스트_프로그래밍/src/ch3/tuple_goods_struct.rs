struct Item(sString, i64);

fn main() {
    let banana = Item(String::from("바나나"), 1000);
    let apple = Item(String::from("사과"), 1500);
    let orange = Item(String::from("오렌지"), 2000);

    let itesm = vec![banana, apple, orange];
    let total = calculate_total(&itesm);
    println!("총 가격: {}", total);
}

fn print_tuple(item: &Item) {
    println!("이름: {}, 가격: {}", item.0, item.1);
}

fn calculate_total(items: &Vec<Item>) -> i64 {
    let mut total = 0;
    for item in items {
        total += item.1;
    }
    total
}
