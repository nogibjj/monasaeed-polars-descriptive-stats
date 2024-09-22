from main import *
import os

def test_get_descriptive_statistics():
    summary = get_descriptive_statistics('price')
    assert round(summary['mean'], 6) == 3932.799722  # mean
    assert summary['median'] == 2401.0  #median
    assert round(summary['std_dev'], 6) == 3989.439738  # std
    assert round(summary['variance'], 6) == 15915629.424301 #variance

def test_generate_carat_price_scatter_plot():
    # Check if the image file is created
    generate_carat_price_scatter_plot(save_as_image=True)
    assert os.path.exists("carat_price_scatter_plot.png")

def test_get_summary_statistics():
    summary = get_summary_statistics()
    # Validate the output markdown includes key statistics
    assert "## Diamonds Dataset Summary Statistics" in summary
    assert "### Descriptive Statistics:" in summary
    assert "mean" in summary
    assert "std" in summary

def test_save_summary_report_to_markdown():
    save_summary_report_to_markdown()
    assert os.path.exists("diamonds_summary_report.md")

if __name__ == '__main__':
    test_get_descriptive_statistics()
    test_generate_carat_price_scatter_plot()
    test_get_summary_statistics()
    test_save_summary_report_to_markdown()