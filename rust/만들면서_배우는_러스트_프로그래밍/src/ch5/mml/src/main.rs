mod mml_parser;
mod wave_writer;

fn main() {
    let mml = format!(
        "{}{}",
        "o4 l4 g l8 ee g e l4 cd l8 edce l4 gs",
        "o5 l8 c o4 l8 g o5 l8 c o4 g o5 c o4 g l4 e g l8 d fed l4 c"
    );

    let notes = mml_parser::parse(mml);
    let bpm = 120.0;
    wave_writer::write("rabbit.wav", notes, bpm);
}
