enum Currency {
    Currency100(isize),
    Currency500(isize),
    Currency1000(isize),
    Currency5000(isize),
    Currency10000(isize),
    Currency50000(isize),
}

impl Currency {
    fn value(&self) -> isize {
        match self {
            Currency::Currency100(v) => v * 100,
            Currency::Currency500(v) => v * 500,
            Currency::Currency1000(v) => v * 1000,
            Currency::Currency5000(v) => v * 5000,
            Currency::Currency10000(v) => v * 10000,
            Currency::Currency50000(v) => v * 50000,
        }
    }
}

fn main() {
    let wallet = vec![
        Currency::Currency100(1),
        Currency::Currency500(2),
        Currency::Currency1000(3),
        Currency::Currency5000(4),
        Currency::Currency10000(5),
        Currency::Currency50000(6),
    ];

    let total = wallet.iter().fold(0, |acc, x| acc + x.value());
    println!("total: {}", total);
}
