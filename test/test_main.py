import doc_pytest.main as m

def test_add():
    result = m.add(5 , 5)
    assert result == 10

def test_divide():
    result = m.divide(5, 5)
    assert result == 1