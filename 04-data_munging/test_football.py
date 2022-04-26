from football import remove_slashes

def test_remove_slashes():
    text = ["Hello-", "----"]
    result = remove_slashes(text)
    assert result == ["Hello"]
