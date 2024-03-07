from ReadWriteMemory import *
from baseAddress import *

# name of the process you want to handle
PROCESS_NAME = "proccess.exe"

rwm = ReadWriteMemory()
base_address = BaseAddress(PROCESS_NAME)

# opening the process
process = rwm.get_process_by_name(PROCESS_NAME)
process.open()

# getting base address pointer + offset array
# replace address '0x00000000' and offsets
pointer = process.get_pointer(base_address.get() + 0x00000000, offsets=[0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F])

# reading the pointer value
value = process.read(pointer)
print(f"value: {value}")

# overriding the pointer value by 10 <int>
process.write(pointer, 10)
