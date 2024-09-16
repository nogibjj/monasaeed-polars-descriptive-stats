from main import *

def test_get_summary_statistics():
    summary = get_summary_statistics()
    assert summary.loc['count', 'price'] == 53940
    assert round(summary.loc['mean', 'price'], 6) == 3932.799722
    assert round(summary.loc['std', 'price'], 6) == 3989.439738
    assert summary.loc['min', 'price'] == 326
    assert summary.loc['25%', 'price'] == 950
    assert summary.loc['50%', 'price'] == 2401
    assert summary.loc['75%', 'price'] == 5324.25
    assert summary.loc['max', 'price'] == 18823
  
def test_get_mode():
    mode = get_mode()
    assert mode['carat'] == 0.3
    assert mode['cut'] == 'Ideal'
    assert mode['color'] == 'G'
    assert mode['clarity'] == 'SI1'
    assert mode['depth'] == 62.0
    assert mode['table'] == 56.0
    assert mode['price'] == 605
    assert mode['x'] == 4.37
    assert mode['y'] == 4.34
    assert mode['z'] == 2.7

def test_get_variance_std():
    variance, std_dev = get_variance_std()
    assert round(variance, 6) == 15915629.424301
    assert round(std_dev, 6) == 3989.439738

if __name__ == '__main__':
    test_get_summary_statistics()
    test_get_mode()
    test_get_variance_std()