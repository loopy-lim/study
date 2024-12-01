use unicode_segmentation::UnicodeSegmentation;

pub struct NewSubscriber {
    pub email: String,
    pub name: SubscribeName,
}

pub struct SubscribeName(String);

impl SubscribeName {
    pub fn parse(s: String) -> Result<SubscribeName, String> {
        let is_empty_or_whitespace = s.trim().is_empty();
        let is_too_long = s.graphemes(true).count() > 256;

        let forbidden_characters = ['/', '(', ')', '"', '<', '>', '\\', '@', '{', '}'];
        let contains_forbidden_characters =
            s.chars().any(|char| forbidden_characters.contains(&char));
        if is_empty_or_whitespace || is_too_long || contains_forbidden_characters {
            panic!("{} is not a valid subscriber name", s);
        } else {
            Ok(Self(s))
        }
    }
}

impl AsRef<str> for SubscribeName {
    fn as_ref(&self) -> &str {
        &self.0
    }
}
