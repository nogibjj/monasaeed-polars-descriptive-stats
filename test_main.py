from main import divide
def test_divide():
    assert divide(2,2) == 1
    assert divide(1,0) == None
    assert divide(-20,2) == -10
if __name__ == "__main__":
    test_divide()