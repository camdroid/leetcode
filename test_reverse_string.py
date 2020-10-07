# From "The Daily Byte"

def reverse(x: str) -> str:
    return x[::-1]

def test_reverse():
    assert reverse('Cat') == 'taC'
    assert reverse('The Daily Byte') == 'etyB yliaD ehT'
    assert reverse('civic') == 'civic'
