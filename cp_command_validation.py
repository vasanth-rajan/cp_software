from utils import FileRecursiveListing
from helpers import check_if_files_data_integrity_maintained, check_if_all_files_copied


if __name__ == "__main__":

    files_search = FileRecursiveListing()

    src = dst = '/Users/rajvasan/Documents/Work/Training/Ansible/test_ansible'
    src_files = files_search.get_files_from_directory(src)

    # cp(src, dst) copy software does the copy from src tp destination

    dst_files = files_search.get_files_from_directory(dst)

    if check_if_all_files_copied(src_files, dst_files):
        print("All files are copied from src to dst")
        if check_if_files_data_integrity_maintained(src_files, dst_files):
            print('Data integrity maintained')
        else:
            print('Data integrity not maintained')
    else:
        if len(dst_files) > len(src_files):
            print('junk files are copied in dst')
        else:
            print('Some files missing in dst')