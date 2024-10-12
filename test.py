from text import to_upper, to_word_list_isupper
import unittest
from app import rnd, max_num_in_list
from unittest.mock import patch
from app import rm
import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TestText(unittest.TestCase):
    def test_to_upper(self):
        result = to_upper("abcdef")
        self.assertEqual(result, "ABCDEF")
from text import to_upper, to_word_list_isupper
import unittest
from app import rnd, max_num_in_list
from unittest.mock import patch
from app import rm
import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TestText(unittest.TestCase):
    def test_to_upper(self):
        result = to_upper("abcdef")
        self.assertEqual(result, "ABCDEF")

    def test_to_word_list_isupper_true(self):
        result = to_word_list_isupper(['I', 'LOVE', 'YOU'])
        self.assertTrue(result)

    def test_to_word_list_isupper_false(self):
        result = to_word_list_isupper(['i', 'LOVE', 'YOU'])
        self.assertFalse(result)

    def test_to_upper_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(123)

    def test_to_word_list_isupper_type_error(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("not a list")

class TestApp(unittest.TestCase):
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

    def test_rnd_correct_value(self):
        result = rnd(2, 20)
        self.assertIn(result, range(2, 21))

    def test_rnd_not_out_of_range(self):
        result = rnd(2, 20)
        self.assertNotIn(result, [1, 21])

    @patch("app.os.remove")
    def test_rm_delete_file(self, mock_remove):
        rm("somefile1.txt")
        mock_remove.assert_called_once_with("somefile1.txt")

    @patch("src.app.os.path.exists", return_value=True)
    @patch("src.app.os.remove")
    def test_rm_call_remove(self, mock_remove, mock_exists):
        rm("somefile1.txt")
        mock_remove.assert_called_once_with("somefile1.txt")
        mock_exists.assert_called_once_with("somefile1.txt")

    @patch("src.app.os.path.exists", return_value=False)
    def test_rm_file_not_found_error(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            rm("somefile1.txt")
        mock_exists.assert_called_once_with("somefile1.txt")

if __name__ == '__main__':
    unittest.main()

    def test_to_word_list_isupper_true(self):
        result = to_word_list_isupper(['I', 'LOVE', 'YOU'])
        self.assertTrue(result)

    def test_to_word_list_isupper_false(self):
        result = to_word_list_isupper(['i', 'LOVE', 'YOU'])
        self.assertFalse(result)

    def test_to_upper_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(123)

    def test_to_word_list_isupper_type_error(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("not a list")

class TestApp(unittest.TestCase):
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

    def test_rnd_correct_value(self):
        result = rnd(2, 20)
        self.assertIn(result, range(2, 21))

    def test_rnd_not_out_of_range(self):
        result = rnd(2, 20)
        self.assertNotIn(result, [1, 21])

    @patch("app.os.remove")
    def test_rm_delete_file(self, mock_remove):
        rm("somefile1.txt")
        mock_remove.assert_called_once_with("somefile1.txt")

    @patch("src.app.os.path.exists", return_value=True)
    @patch("src.app.os.remove")
    def test_rm_call_remove(self, mock_remove, mock_exists):
        rm("somefile1.txt")
        mock_remove.assert_called_once_with("somefile1.txt")
        mock_exists.assert_called_once_with("somefile1.txt")

    @patch("src.app.os.path.exists", return_value=False)
    def test_rm_file_not_found_error(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            rm("somefile1.txt")
        mock_exists.assert_called_once_with("somefile1.txt")

if __name__ == '__main__':
    unittest.main()
