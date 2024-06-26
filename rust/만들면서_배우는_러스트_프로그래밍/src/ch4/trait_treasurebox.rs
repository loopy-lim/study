trait TreasureBox {
    fn open(&self, key_no: i32) -> bool;
    fn check(&self);
}

struct JewelrayBox {
    key_no: i32,
    price: i32,
}

impl TreasureBox for JewelrayBox {
    fn open(&self, key_no: i32) -> bool {
        self.key_no == key_no
    }

    fn check(&self) {
        println!("보석 상자였다. {} 골드 입수.", self.price);
    }
}

struct TrapBox {
    damage: i32,
}

impl TreasureBox for TrapBox {
    fn open(&self, key_no: i32) -> bool {
        self.damage > 0
    }

    fn check(&self) {
        println!("함정 상자였다. 데미지 {}를 입었다.", self.damage);
    }
}

fn open_box(tbox: &impl TreasureBox, key_no: i32) {
    if !tbox.open(key_no) {
        println!("열쇠가 맞지 않아 상자가 열리지 않는다.");
        return;
    } else {
        tbox.check();
    }
}

fn main() {
    let box1 = JewelrayBox {
        price: 30,
        key_no: 1,
    };

    let box2 = TrapBox { damage: 3 };
    let box3 = JewelrayBox {
        price: 50,
        key_no: 2,
    };

    let my_key = 2;
    open_box(&box1, my_key);
    open_box(&box2, my_key);
    open_box(&box3, my_key);
}
