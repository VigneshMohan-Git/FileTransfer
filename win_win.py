#Windows to Windows File Transfer
import os
import shutil, sys
def Copy(source, destination, include_empty_dirs=True):
    
    source = os.path.abspath(source)
    for p, ds, fs in os.walk(source):
        if include_empty_dirs:
            for d in ds:
                d_path = os.path.join(destination, p[len(source):], d)
                # Make dirs
                if not os.path.isdir(d_path):
                    print('Making {0}'.format(d_path))
                    os.makedirs(d_path)
        for f in fs:
            s_path = os.path.join(p, f)
            d_path = os.path.join(destination, p[len(source) + 1:], f)
            print('Copying {0} -> {1}'.format(s_path, d_path))
            # Make dirs
            if not os.path.isdir(os.path.dirname(d_path)):
                print('Making {0}'.format(d_path))
                os.makedirs(os.path.dirname(d_path))
            # Copy the file
            shutil.copy(s_path, d_path)
            
    print("File Transfer Complete")
            
source = "\\\\10.10.1.50\\DeX_Source_Win\\"
destination = "\\\\10.10.1.100\\DeX_Target_Win\\"

Copy(source, destination, include_empty_dirs=True)