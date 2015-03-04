import subprocess

def run_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()


def devices():
    devices = []
    cmd = ['adb','devices']
    res, err = run_cmd(cmd)
    for line in res.split('\n'):
        if line[-6:]  == 'device':
            devices.append(line.split()[0])
    return devices


def getprop(serial, prop):
    '''
    >>> import re
    >>> match = re.search('(?P<name>.*) (?P<phone>.*)', 'John 123456')
    >>> match.group('name')
    'hah'
    '''
    cmd = ['adb', '-s',serial, 'shell', 'getprop']
    if prop is not None:
        cmd.append(prop)
    res, err = run_cmd(cmd)
    return res


if __name__ == '__main__':
    


    prop = 'ro.build.version.release'
    for device in devices():
        print getprop(device, prop).strip()
    import doctest
    doctest.testmod()