# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import zlib


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class OnwaTuf(KaitaiStruct):
    """TUF is the firmware update file format for older (MK1) ONWA Marine GPS Plotters.
    
    The system seems to be based on an ARM-32 EABI4 Linux 2.6.
    
    During the update process, the updater searches for "*.sh" bash script files
    on the MMC/SD card and executes them in system calls, which seems like
    a perfect chance to gain some more insights into the system.
    
    As can be seen in the Kaitai struct file, some things are still unclear,
    but basic extraction of files from the firmware update is possible.
    
    .. seealso::
       Source - https://github.com/speters/onwatuf/
    
    
    .. seealso::
       Source - https://onwamarine.com/support-and-download/
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x54\x55\x46\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x54\x55\x46\x00", self.magic, self._io, u"/seq/0")
        self.file_offset = self._io.read_u4le()
        self._raw_tuf_header = self._io.read_bytes(((self.file_offset - 4) - 4))
        _io__raw_tuf_header = KaitaiStream(BytesIO(self._raw_tuf_header))
        self.tuf_header = OnwaTuf.TTufHeader(_io__raw_tuf_header, self, self._root)
        self.tuf_entries = []
        i = 0
        while not self._io.is_eof():
            self.tuf_entries.append(OnwaTuf.TTufEntry(self._io, self, self._root))
            i += 1


    class TTufHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tuf_id = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")
            self.tuf_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")


    class TTufEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filename = (KaitaiStream.bytes_terminate(self._io.read_bytes(130), 0, False)).decode(u"UTF-8")
            self.stuff = self._io.read_u2le()
            self.stuff2 = self._io.read_u4le()
            self.file_len = self._io.read_u4le()
            self.file_len2 = self._io.read_u2le()
            self.stuff3 = self._io.read_bytes(2)
            if self.file_len > 0:
                self._raw_file_contents = self._io.read_bytes((self.file_len + self.file_len2))
                self.file_contents = zlib.decompress(self._raw_file_contents)



    class TTufEntries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tuf_entry = []
            i = 0
            while not self._io.is_eof():
                self.tuf_entry.append(OnwaTuf.TTufEntry(self._io, self, self._root))
                i += 1




