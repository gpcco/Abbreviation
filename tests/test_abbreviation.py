import pytest

from abbreviation import abbreviate, abbreviate_multiple


def test_produces_abbreviations_of_varying_lengths():
    """The length of the abbreviation can be set."""
    word = "Friday"
    assert len(abbreviate(word=word, length=3)) == 3
    assert len(abbreviate(word=word, length=2)) == 2
    assert len(abbreviate(word=word, length=1)) == 1


def test_abbreviation_longer_than_word_stops_at_wordlength():
    """Abbreviation lengths are capped at the length of the word."""
    word = "Friday"
    assert len(abbreviate(word=word, length=len(word) + 1)) == len(word)


def test_length_lower_than_one_returns_None_and_warning(capsys):
    """A length of less than one results in None and a printed warning."""
    word = "Friday"
    abbreviation = abbreviate(word=word, length=0)
    captured = capsys.readouterr()
    assert abbreviation is None
    assert captured.out == "Given length must be higher than 0."


def test_whitespace_serves_as_a_divider():
    """Whitespace is used to find abbreviations."""
    word = "Friday"
    assert abbreviate(word=word, length=3) == "Fri"
    word = "Fri day"
    assert abbreviate(word=word, length=3) == "Frd"


def test_show_all_possible_abbreviations():
    """All options provides all possible abbreviations of the given word."""
    word = "Friday"
    abbreviations = abbreviate(word, length=1, all=True)
    assert abbreviations == [c for c in word]


def test_abbreviate_multiple_avoids_duplicates():
    """Abbreviation tries to avoid duplication in the abbreviations."""
    words = ["Monday", "Moon", "Money", "Monastery", "Monopoly", "Monaco"]
    abbreviations = abbreviate_multiple(words=words, length=3)
    assert len(abbreviations) == len(list(set(abbreviations)))
