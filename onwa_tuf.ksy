meta:
  id: onwa_tuf
  file-extension: tuf
  title: ONWA Marine GPS Plotter firmware TUF update
  endian: le
doc: |
  TUF is the firmware update file format for older (MK1) ONWA Marine GPS Plotters.
  
  The system seems to be based on an ARM-32 EABI4 Linux 2.6.
  
  During the update process, the updater searches for "*.sh" bash script files
  on the MMC/SD card and executes them in system calls, which seems like
  a perfect chance to gain some more insights into the system.
  
  As can be seen in the Kaitai struct file, some things are still unclear,
  but basic extraction of files from the firmware update is possible.
doc-ref:
  - https://github.com/speters/onwatuf/
  - https://onwamarine.com/support-and-download/
seq:
  - id: magic
    contents: ['TUF', 0x00] # TUF
  - id: file_offset
    type: u4
  - id: tuf_header
    type: t_tuf_header
    size: file_offset -4 -4
  - id: tuf_entries
    type: t_tuf_entry
    repeat: eos
types:
  t_tuf_header:
    seq:
      - id: tuf_id
        type: str
        encoding: UTF-8
        terminator: 0
        size: 8
      - id: tuf_version
        type: str
        encoding: UTF-8
        terminator: 0
        size: 8
  t_tuf_entry:
    seq:
      - id: filename
        type: str
        size: 130
        encoding: UTF-8
        terminator: 0
      - id: stuff
        type: u2
      - id: stuff2
        type: u4
      - id: file_len
        type: u4
      - id: file_len2
        type: u2
      - id: stuff3
        size: 2
      - id: file_contents
        size: file_len + file_len2
        process: zlib
        if: file_len > 0
  t_tuf_entries:
    seq:
      - id: tuf_entry
        type: t_tuf_entry
        repeat: eos
