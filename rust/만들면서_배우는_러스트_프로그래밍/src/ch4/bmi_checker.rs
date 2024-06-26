fn main() {
    let body = Body::new(163.0, 75.2, "성은");
    body.print_result();

    let body = Body::new(158.2, 55.0, "성은");
    body.print_result();

    let body = Body::new(175.2, 54.2, "성은");
    body.print_result();
}

struct BmiRange {
    min: f64,
    max: f64,
    label: String,
}

impl BmiRange {
    fn new(min: f64, max: f64, label: &str) -> BmiRange {
        BmiRange {
            min,
            max,
            label: label.to_string(),
        }
    }

    fn test(&self, bmi: f64) -> bool {
        self.min <= bmi && bmi < self.max
    }
}

struct Body {
    height: f64,
    weight: f64,
    name: String,
}

impl Body {
    fn new(height: f64, weight: f64, name: &str) -> Body {
        Body {
            height,
            weight,
            name: name.to_string(),
        }
    }

    fn bmi(&self) -> f64 {
        self.weight / (self.height / 100.0).powf(2.0)
    }

    fn print_result(&self) {
        let bmi = self.bmi();
        let ranges = vec![
            BmiRange::new(0.0, 18.5, "마른체형"),
            BmiRange::new(18.5, 23.0, "표준"),
            BmiRange::new(23.0, 25.0, "과체중"),
            BmiRange::new(25.0, 30.0, "비만"),
            BmiRange::new(30.0, f64::INFINITY, "고도비만"),
        ];

        for range in ranges {
            if range.test(bmi) {
                println!("{}님은 {}입니다.", self.name, range.label);
                return;
            }
        }
    }
}
