import tempfile
import unittest
from pathlib import Path

from books import parse_feed, update_about


class ReadingUpdateTests(unittest.TestCase):
    def test_unreviewed_current_book_is_included(self):
        feed = b"<rss><channel><item><title>A book</title><user_rating>0</user_rating></item></channel></rss>"
        self.assertEqual(len(parse_feed(feed, "Currently Reading")), 1)
        self.assertEqual(parse_feed(feed, "Read"), [])

    def test_about_update_escapes_limits_and_preserves_surrounding_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "about.html"
            path.write_text('Before <!-- current-reading:start -->Old<!-- current-reading:end --> After')
            books = [
                {"title": "<Book & One>", "author": "A & B", "status": "Currently Reading"},
                {"title": "Second", "author": "", "status": "Currently Reading"},
                {"title": "Third", "status": "Currently Reading"},
            ]
            self.assertTrue(update_about(books, path))
            result = path.read_text()
            self.assertIn('<em>&lt;Book &amp; One&gt;</em> by A &amp; B and <em>Second</em>.', result)
            self.assertNotIn("Third", result)
            self.assertTrue(result.startswith("Before "))
            self.assertTrue(result.endswith(" After"))
            self.assertFalse(update_about(books, path))
            self.assertFalse(update_about([], path))
            self.assertEqual(path.read_text(), result)

    def test_missing_region_fails_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "about.html"
            path.write_text("Original")
            with self.assertRaises(ValueError):
                update_about([{"title": "Book", "status": "Currently Reading"}], path)
            self.assertEqual(path.read_text(), "Original")
