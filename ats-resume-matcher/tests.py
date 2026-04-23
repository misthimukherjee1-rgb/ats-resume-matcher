Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from app import tokenize, keyword_stats
... 
... def test_tokenize_removes_stopwords():
...     words = tokenize("This is a test of the keyword matcher")
...     assert "this" not in words
...     assert "test" in words
... 
... def test_keyword_stats_basic():
...     resume = "Python SQL HTML"
...     jd = "Python SQL Java"
...     score, common, missing, _ = keyword_stats(resume, jd)
...     assert "python" in common
...     assert "java" in missing
