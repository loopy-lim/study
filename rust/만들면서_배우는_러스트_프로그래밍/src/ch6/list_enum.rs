enum Node {
    Empty,
    Cons(i64, Box<Node>),
}

use Node::{Cons, Empty};
fn node(v: i64, link: Box<Node>) -> Box<Node> {
    Box::new(Cons(v, link))
}

fn main() {
    let c = node(10, node(20, node(30, Box::new(Empty))));

    let mut p: &Box<Node> = &c;
    loop {
        let cur_node: &Node = &**p;
        match cur_node {
            Empty => break,
            Cons(data, link) => {
                println!("{}", data);
                p = link;
            }
        }
    }
}
