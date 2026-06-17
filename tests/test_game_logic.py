from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert "Win" in result

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert "Too High" in result 

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert "Too Low" in result

def test_guess_way_too_high():
    # If secret is 42 and guess is 99, hint should be "Too High"
    result = check_guess(99, 42)
    assert "Too High" in result 
