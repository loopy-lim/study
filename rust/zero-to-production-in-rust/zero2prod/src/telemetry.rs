use tracing::Subscriber;
use tracing_bunyan_formatter::BunyanFormattingLayer;
use tracing_subscriber::fmt::MakeWriter;

pub fn get_subscriber<Sink>(
    name: String,
    env_filter: String,
    sink: Sink,
) -> impl Subscriber + Sync + Send
where
    Sink: for<'a> MakeWriter<'a> + Send + Sync + 'static,
{
    BunyanFormattingLayer::new(name, sink)
}
