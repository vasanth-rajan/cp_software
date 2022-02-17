# cp_software

Run the below python file to validate the copy operation
python cp_command_validation.py


To run unit tests:- 
(base) cp_software % python -m unittest -vv
test_check_if_all_files_copied (test_helpers.TestHelpers)
test to check all the files are copied from src to dst ... ok
test_check_if_all_files_not_copied (test_helpers.TestHelpers)
test to check all the files are not copied from src to dst ... ok
test_check_if_files_data_integrity_maintained (test_helpers.TestHelpers)
test to check the data integrity between src / dst ... ok
test_check_if_files_data_integrity_not_maintained (test_helpers.TestHelpers)
test to check the data integrity not maintained between src / dst ... list of corrupt files/dirs
ok
test_get_md5 (test_helpers.TestHelpers)
test to verify the md5 checksum of a file ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.004s

OK
(base) cp_software % 
