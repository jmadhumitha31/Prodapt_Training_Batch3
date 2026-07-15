from words import count_words, unique_words, reverse_word

def test_count_words():
    assert count_words("hello world hello")==3
def test_unique_words():
    assert unique_words("hello world hello")=={"hello","world"}
def test_reverse_word():
    assert reverse_word("abc","madhu")==["cba","uhdam"]
def edge_case_empty_string():
    assert count_words("")==0
    assert unique_words("")==set()
    assert reverse_word("")==[]
