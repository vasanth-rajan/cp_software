import os.path
import unittest
import helpers
import utils


class TestHelpers(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'test1.txt')
        self.src_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'src')
        self.dst_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'dst')

    def test_get_md5(self):
        """test to verify the md5 checksum of a file"""
        h = helpers._get_md5_checksum(self.test_file)
        self.assertEqual(h,'18fc40d2ab81177e24e24610a1963f4e')

    def test_check_if_files_data_integrity_maintained(self):
        """test to check the data integrity between src / dst """
        test_obj = utils.FileRecursiveListing()
        src_files = test_obj.get_files_from_directory(self.src_dir)
        dst_files = src_files

        h = helpers.check_if_files_data_integrity_maintained(src_files, dst_files)
        self.assertEqual(h, True)

    def test_check_if_files_data_integrity_not_maintained(self):
        """test to check the data integrity not maintained between src / dst """
        test_obj = utils.FileRecursiveListing()
        src_files = test_obj.get_files_from_directory(self.src_dir)
        dst_files = test_obj.get_files_from_directory(self.dst_dir)

        h = helpers.check_if_files_data_integrity_maintained(src_files, dst_files)
        self.assertEqual(h, False)

    def test_check_if_all_files_copied(self):
        """test to check all the files are copied from src to dst"""
        test_obj = utils.FileRecursiveListing()
        src_files = test_obj.get_files_from_directory(self.src_dir)
        dst_files = src_files

        h = helpers.check_if_all_files_copied(src_files, dst_files)
        self.assertEqual(h, True)

    def test_check_if_all_files_not_copied(self):
        """test to check all the files are not copied from src to dst"""
        test_obj = utils.FileRecursiveListing()
        src_files = test_obj.get_files_from_directory(self.src_dir)
        dst_files = test_obj.get_files_from_directory(self.dst_dir)

        h = helpers.check_if_all_files_copied(src_files, dst_files)
        self.assertEqual(h, False)





