import os
from subprocess import Popen, PIPE, DEVNULL

class PCInterface():
    def __init__(self, folder: str) -> None:
        self.folder_n = folder


    def create_file(self, f_name, f_ext):
        full_path = os.path.join(self.folder_n, f_name+'.'+f_ext)
        with open(full_path, 'x') as _: 
            pass

    def update_file_c(self, f_name, update):
        full_path = os.path.join(self.folder_n, f_name)
        with open(full_path, 'w') as f: 
            f.write(update)

    
    def update_file(self, f_name, update):
        full_path = os.path.join(self.folder_n, f_name)
        with open(full_path, 'a') as f: 
            f.write(update)


    def delete_file(self, f_name):
        os.remove(os.path.join(self.folder_n, f_name))


    def run_os_cmd(self, cmd, ret_out=True, ret_err=True, ret_code=True):
        popen = Popen(cmd, stdout=PIPE, stderr=PIPE)
        popen.wait()
        code = popen.returncode
        out, err = popen.communicate()

        if ret_out and ret_err and ret_code:
            return out, err, code
        if not ret_out and ret_err and ret_code:
            return err, code
        if ret_out and not ret_err and ret_code:
            return out, code
        if ret_out and ret_err and not ret_code:
            return out, err
        if not ret_out and not ret_err and not ret_code:
            pass