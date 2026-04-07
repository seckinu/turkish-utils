import turkish_utils as t

if __name__ == "__main__":
    assert t.syllabilize("masa") == ["ma", "sa"]
    assert t.toUpper("ABCcĞğ") == "ABCCĞĞ"
    assert t.toLower("ABCcĞğ") == "abccğğ"
