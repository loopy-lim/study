use unicode_segmentation::UnicodeSegmentation;

pub struct NewSubscriber {
    pub email: String,
    pub name: SubscribeName,
}

#[derive(Debug)]
pub struct SubscribeName(String);

impl SubscribeName {
    pub fn parse(s: String) -> Result<SubscribeName, String> {
        let is_empty_or_whitespace = s.trim().is_empty();
        let is_too_long = s.graphemes(true).count() > 256;

        let forbidden_characters = ['/', '(', ')', '"', '<', '>', '\\', '@', '{', '}'];
        let contains_forbidden_characters =
            s.chars().any(|char| forbidden_characters.contains(&char));
        if is_empty_or_whitespace || is_too_long || contains_forbidden_characters {
            Err(format!("{} is not a valid subscriber name", s))
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

#[cfg(test)]
mod tests {
    use crate::domain::SubscribeName;
    use claim::{assert_err, assert_ok};

    #[test]
    fn a_256_grapheme_long_name_is_valid() {
        let name = "ɑ".repeat(256);
        assert_ok!(SubscribeName::parse(name));
    }

    #[test]
    fn a_name_longer_then_256_graphemes_is_rejected() {
        let name = "a".repeat(257);
        assert_err!(SubscribeName::parse(name));
    }

    #[test]
    fn whitespace_only_name_is_rejected() {
        let name = " ".to_string();
        assert_err!(SubscribeName::parse(name));
    }

    #[test]
    fn empty_name_is_rejected() {
        let name = "".to_string();
        assert_err!(SubscribeName::parse(name));
    }

    #[test]
    fn names_containing_an_invalid_character_are_rejected() {
        for name in &['/', '(', ')', '"', '<', '>', '\\', '@', '{', '}'] {
            let name = name.to_string();
            assert_err!(SubscribeName::parse(name));
        }
    }

    #[test]
    fn a_valid_name_is_parsed_successfully() {
        let name = "loopy-lim".to_string();
        assert_ok!(SubscribeName::parse(name));
    }
}
