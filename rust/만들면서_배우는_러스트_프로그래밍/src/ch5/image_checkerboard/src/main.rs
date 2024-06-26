use image;

fn main() {
    let white = image::Rgb::<u8>([255, 255, 255]);
    let red = image::Rgb::<u8>([255, 90, 90]);
    let w = 64;

    let draw = |x, y| {
        let (xi, yi) = (x / w, y / w);
        match (xi % 2, yi % 2) {
            (0, 0) | (1, 1) => white,
            _ => red,
        }
    };

    let img = image::ImageBuffer::from_fn(512, 512, draw);
    img.save("checkerboard.png").unwrap();
}
