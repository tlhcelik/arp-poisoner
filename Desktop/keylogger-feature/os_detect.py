from os import name as os_name
from getpass import getuser as os_user_name


class OsDetect:
    def __init__(self):

        self.FILE = '*'
        self.UNAME = os_user_name()

    @property
    def get_os_for_file_name(self):
        """
        example using:
        [new.py]
        from os_detect import OsDetect
        obj = OsDetect()
        print obj.get_os_for_file_name
        output in linux -> /home/malc
        output in windows -> C:\Document End Settings \malc\

        :return: str
        """
        if os_name == 'posix':
            self.FILE = '/home/{0}/'.format(self.UNAME)

        if os_name == 'nt':
            self.FILE = r"C:\Document End Settings\{0}".format(self.UNAME)

        return self.FILE
