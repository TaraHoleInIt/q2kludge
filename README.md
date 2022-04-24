### Kludge: Quartus II on Apple Silicon

I have no idea what I'm doing lol.

#### Requirements:
- Rosetta 2
- Quartus II 13.0sp1 for Windows
- Wine64
- Python 3
- Edalize

#### Quartus II:
This needs a copy of the Quartus II software which must be installed to obtain the delicious, gooey binaries within. This can be done on a real Windows machine, using a Windows VM, using a ReactOS VM, or if you are able to run the 32bit installer under WINE.

I grabbed the quartus directory from the installation and dropped it in my home directory. You can probably safely delete everything in the bin directory since it's all 32bit anyway.

Copy qs.sh and qs_pgm.sh to the quartus bin directory.
Create the following symlinks:

```
ln -s qs.sh quartus_asm
ln -s qs.sh quartus_map
ln -s qs.sh quartus_fit
ln -s qs.sh quartus_sh
ln -s qs.sh quartus_sta
ln -s qs.sh quartus_cpf
ln -s qs_pgm.sh quartus_pgm
```

#### Using the Python script:
I am not good at Python.
That being said, this might be good enough for now.

Put the verilog sources in a directory called "src", and all board related files in a directory called "board".

Put q2.py wherever your project is going to be.
Run it and pray that it works.

###### Clean build files:
`python3 q2.py clean`

##### Configure build:
`python3 q2.py configure`

##### Build build build build build:
`python3 q2.py build`

##### Load onto FPGA:
`python3 q2.py run`

##### DO EVERTHING:
`python3 q2.py clean configure build run`
