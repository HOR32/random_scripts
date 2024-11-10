import fcntl
import os
CDROM = "/dev/sr0"
while True:
    fd = os.open(CDROM, os.O_RDONLY | os.O_NONBLOCK)
    rv = fcntl.ioctl(fd, 0x5326)
    os.close(fd)
    if rv == 4:
        os.system('mpv --no-audio-display --osd-level=0 -cdrom-device /dev/sr0 cdda:// > /dev/null 2>&1  & vis ')
        break

