import os


class FileRecursiveListing(object):
    """Recurse each directory of a path and store the searched files in a list"""

    def _recurse(self, parent_path, files_list, output_files_list):
        """Recurse the directory and find the available files in each subdirectory.
        :param parent_path: Root directory.
        :param files_list: list containing the files in a directory.
        :param output_files_list: output list to store the found files.
        :return: files list.
        """

        if len(files_list) == 0:
            return
        else:
            for sub_path in files_list:
                full_path = os.path.join(parent_path, sub_path)

                output_files_list.append(full_path)
                if not os.path.isfile(full_path):
                    self._recurse(full_path, os.listdir(full_path), output_files_list)

    def get_files_from_directory(self, path):
        """Get files from a directory
        :param path: path where files to be searched.
        :return: output files_list.
        """""

        out_list = []
        # Opting list over dict since we have absolute path of the files and directories in the output.
        # Also, list is easy to iterate for md5 validation
        self._recurse(path, os.listdir(path), out_list)
        return out_list
