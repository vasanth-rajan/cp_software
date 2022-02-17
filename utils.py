import os

class FileRecursiveListing(object):
    """Recurse each directory of a path and store the searched files in a list"""

    def _recurse(self, parent_path, files_list, output_buf):
        """Recurse the directory and find the available files in each subdirectory.
        :param parent_path: Root directory.
        :param files_list: list containing the files in a directory.
        :param output_buf: output list to store the found files.
        :return: files list.
        """

        if len(files_list) == 0:
            return
        else:
            for sub_path in files_list:
                full_path = os.path.join(parent_path, sub_path)

                if os.path.isfile(full_path):
                    output_buf.append(full_path)
                else:
                    self._recurse(full_path, os.listdir(full_path), output_buf)

    def get_files_from_directory(self, path):
        """Get files from a directory
        :param path: path where files to be searched.
        :return: files_list
        """""

        buf = []
        self._recurse(path, os.listdir(path), buf)
        return buf