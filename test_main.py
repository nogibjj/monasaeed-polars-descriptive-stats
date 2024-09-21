from main import *

def test_get_summary_statistics():
    summary = get_summary_statistics()
    # Convert 'summary' to a dictionary or access elements using Polars' indexing
    summary_dict = summary.to_dict(as_series=False)
    
    # Access values from the summary dictionary
    assert summary_dict['price'][0] == 53940  # count
    assert round(summary_dict['price'][1], 6) == 3932.799722  # mean
    assert round(summary_dict['price'][2], 6) == 3989.439738  # std
    assert summary_dict['price'][3] == 326  # min
    assert summary_dict['price'][4] == 950  # 25%
    assert summary_dict['price'][5] == 2401  # 50%
    assert summary_dict['price'][6] == 5324.25  # 75%
    assert summary_dict['price'][7] == 18823  # max
  
def test_get_mode():
    mode = get_mode()
    mode_dict = mode.to_dict(as_series=False)

    # Access values from the mode dictionary
    assert mode_dict['carat'][0] == 0.3
    assert mode_dict['cut'][0] == 'Ideal'
    assert mode_dict['color'][0] == 'G'
    assert mode_dict['clarity'][0] == 'SI1'
    assert mode_dict['depth'][0] == 62.0
    assert mode_dict['table'][0] == 56.0
    assert mode_dict['price'][0] == 605
    assert mode_dict['x'][0] == 4.37
    assert mode_dict['y'][0] == 4.34
    assert mode_dict['z'][0] == 2.7

def test_get_variance_std():
    variance, std_dev = get_variance_std()
    assert round(variance, 6) == 15915629.424301
    assert round(std_dev, 6) == 3989.439738

if __name__ == '__main__':
    test_get_summary_statistics()
    test_get_mode()
    test_get_variance_std()
