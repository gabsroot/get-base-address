"""
project: get-base-address
version: 1.0
developed by: https://github.com/gabsroot
"""

import ctypes
import os

class BaseAddress:
    def __init__(self, process_name: str) -> None:
        self.processHandle = self.process_handle(process_name)

    def process_handle(self, process_name: str):
        # lookup handle by process name
        process_ids = (ctypes.c_ulong * 1024)()
        process_count = ctypes.c_ulong()
        
        ctypes.windll.psapi.EnumProcesses(ctypes.byref(process_ids), ctypes.sizeof(process_ids), ctypes.byref(process_count))

        for i in range(process_count.value):
            process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, process_ids[i])

            if process_handle:
                image_file_name = (ctypes.c_char * 1024)()

                if ctypes.windll.psapi.GetProcessImageFileNameA(process_handle, image_file_name, 1024) > 0:
                    filename = os.path.basename(image_file_name.value)

                    if filename.decode('utf-8') == process_name:
                        return process_handle
                    
                ctypes.windll.kernel32.CloseHandle(process_handle)

    def get(self) -> int:
        # returns the base address of the process
        MODULEINFO = ctypes.c_ulonglong * 3

        hModule = ctypes.c_void_p()
        cbNeeded = ctypes.c_ulong()
        module_info = MODULEINFO()

        ctypes.windll.psapi.EnumProcessModulesEx(self.processHandle, ctypes.byref(hModule), ctypes.sizeof(hModule), ctypes.byref(cbNeeded), 0x03)
        ctypes.windll.psapi.GetModuleInformation(self.processHandle, hModule, ctypes.byref(module_info), ctypes.sizeof(module_info))

        return module_info[0]