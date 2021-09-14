# onwatuf
TUF firmware file format dissection for ONWA Marine GPS Plotters (MK1)

ONWA Marine GPS plotters from the older MK1 series (like KCombo7) use a "TUF" firmware update format, which is basically a nunch of deflated files smushed together.

![Graphviz display of TUF file format](tuf.png)

In this repository, you will find a basic file format description as a [Kaitai](https://kaitai.io) KSY file.

Additionally, there is a simple Python script based on Kaitai to extract the files from the TUF firmware update file.
