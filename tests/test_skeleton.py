from mock_api.main import func

__author__ = "AlTosterino"
__copyright__ = "AlTosterino"
__license__ = "MIT"


def test_fib():
    """API Tests"""
    assert func(1, 1) == 2


# def test_main(capsys):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts agains stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     main(["7"])
#     captured = capsys.readouterr()
#     assert "The 7-th Fibonacci number is 13" in captured.out
