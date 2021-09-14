# onwatuf
TUF firmware file format dissection for ONWA Marine GPS Plotters (MK1)

ONWA Marine GPS plotters from the older MK1 series (like KCombo7) use a "TUF" firmware update format, which is basically a nunch of deflated files smushed together.

![Graphviz display of TUF file format](tuf.png)

In this repository, you will find a basic file format description as a [Kaitai](https://kaitai.io) KSY file.

Additionally, there is a simple Python script based on Kaitai to extract the files from the TUF firmware update file.

## Observations
  * Plotter is based on ARM-32 system running Linux 2.16
  * `*.sh` bash shell scripts on MMC/SD-card will be executed during the update - the perfect chance to gain full control
  * later models use a different encrypted or at least obfuscated `xUF` file format, which is not covered here
  
### Possible "attacks"
 * Write a shell script which makes a complete dump of the firmware to MMC/SD-card. The mountpoint `/KP6XX/MMC` might differ, so check for mounted filesystems instead of a hardcoded path.
 * Check similar shell script approach on MK2 plotters to work out a decryption/deobfuscation method based on info from the files.
 * Get info about K-Chart file format
 * Get info about implementation of C-Map and Navionics charts (not on all models)
 * Ask manufacturer for sources of used software which is GPL and similarly licensed
