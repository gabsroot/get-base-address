# get-base-address

a tool to get the base address of a process to complement [@vsantiago113/ReadWriteMemory](https://github.com/vsantiago113/ReadWriteMemory) tool.
## usage

```python
from ReadWriteMemory import *
from baseAddress import *

# name of the process you want to handle
PROCESS_NAME = "Multi Theft Auto.exe"

rwm = ReadWriteMemory()
base_address = BaseAddress(PROCESS_NAME)

process = rwm.get_process_by_name(PROCESS_NAME)
process.open()

# getting pointer from base address + offsets
# replace address '0x00034A10' and offsets with the desired one
pointer = process.get_pointer(base_address.get() + 0x00034A10, offsets=[0x38, 0x30, 0x34, 0x0, 0x0, 0x1C, 0xDB8])

# reading the pointer value
value = process.read(pointer)
print(f"value: {value}")

# overriding the pointer value by 10 (int)
process.write(pointer, 10)
```

## authors

- [@gabsroot](https://www.github.com/gabsroot)