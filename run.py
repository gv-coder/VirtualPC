from utils import d_machine
from sys import platform
from utils.errors import IncompatiblePlatformError
from version import __version__

if __name__ == '__main__':
    if platform.startswith('win'):
        d_machine.run()

    else:
        raise IncompatiblePlatformError(f'The platform you are using ({platform} to be precise) is not compatible with VirtualPC v{__version__}')