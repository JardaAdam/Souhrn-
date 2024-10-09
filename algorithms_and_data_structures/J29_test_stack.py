from J29_stack import brackets, brackets2


def test_brackets():
    assert brackets("()") is True
    assert brackets("(())") is True
    assert brackets("(()(") is False
    assert brackets(")()") is False
    assert brackets("") is True
    assert brackets("()()") is True
    assert brackets("())(") is False


def test_brackets2():
    assert brackets2("()") is True
    assert brackets2("(())") is True
    assert brackets2("(()") is False
    assert brackets2(")(") is False
    assert brackets2("") is True
    assert brackets2("()()") is True
    assert brackets2("())(") is False

    # Additional test cases for brackets2 function with different types of brackets
    assert brackets2("([])") is True
    assert brackets2("([][{}])") is True
    assert brackets2("({[]<[]>}())") is True
    assert brackets2("([)]") is False
    assert brackets2("({[][<]>}())") is False
    assert brackets2("{[}") is False
    assert brackets2("{[()]}") is True
    assert brackets2("({[}])") is False
