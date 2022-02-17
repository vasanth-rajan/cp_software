import hashlib
import os


def _get_md5_checksum(filename):
    """Get MD5 checksum of a file
    :param filename: The filename of which we need to obtain MD5 Sum
    :return: MD5 digest
    """
    h = hashlib.md5()
    chunk_num_blocks = 128
    with open(filename, 'rb') as f:
        while chunk := f.read(chunk_num_blocks * h.block_size):
            h.update(chunk)
    return h.hexdigest()


def check_if_files_data_integrity_maintained(src_files, dst_files):
    """
    Compare the checksum of each files in src and dst directory.
    :param src_files: Source file list
    :param dst_files: Destination file list
    :return: Boolean value
    """
    corrupt_files_list = []
    data_integrity_maintained = False
    for count in range(len(dst_files)):
        if os.path.isfile(src_files[count]):
            if _get_md5_checksum(src_files[count]) == _get_md5_checksum(dst_files[count]):
                data_integrity_maintained = True
            else:
                print('list of corrupt files/dirs')
                corrupt_files_list.append(src_files[count])
                return False
    return data_integrity_maintained

def check_if_all_files_copied(src_files, dst_files):
    """
    Check if all the files are copied from src to dst
    :param src_files: source files list
    :param dst_files: destination files list
    :return: Boolean
    """

    if len(src_files) == len(dst_files):
        return True
    return False

