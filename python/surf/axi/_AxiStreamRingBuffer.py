#-----------------------------------------------------------------------------
# Title      : PyRogue AXI-Lite Ring Buffer Module
#-----------------------------------------------------------------------------
# Description:
# PyRogue AXI-Lite Ring Buffer Module
#-----------------------------------------------------------------------------
# This file is part of the 'SLAC Firmware Standard Library'. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the 'SLAC Firmware Standard Library', including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import pyrogue as pr

import time

class AxiStreamRingBuffer(pr.Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add(pr.RemoteVariable(
            name         = 'BufferLength',
            description  = 'Length of ring buffer',
            offset       = 0x0,
            bitSize      = 20,
            bitOffset    = 0,
            mode         = 'RO',
            pollInterval = 1,
        ))

        self.add(pr.RemoteVariable(
            name         = 'RAM_ADDR_WIDTH_G',
            description  = 'Ring Buffer RAM Width configuration',
            offset       = 0x0,
            bitSize      = 8,
            bitOffset    = 20,
            mode         = 'RO',
            disp         = '{:d}',
        ))

        self.add(pr.RemoteVariable(
            name         = 'ExtBufferClear',
            description  = 'External Buffer Clear Status',
            offset       = 0x0,
            bitSize      = 1,
            bitOffset    = 28,
            mode         = 'RO',
            pollInterval = 1,
        ))

        self.add(pr.RemoteVariable(
            name         = 'ExtBufferEnable',
            description  = 'External Buffer Enable Status',
            offset       = 0x0,
            bitSize      = 1,
            bitOffset    = 29,
            mode         = 'RO',
            pollInterval = 1,
        ))

        self.add(pr.RemoteVariable(
            name         = 'TrigCnt',
            description  = 'current value of the trigger counter',
            offset       = 0x4,
            bitSize      = 32,
            bitOffset    = 0,
            mode         = 'RO',
            pollInterval = 1,
        ))

        self.add(pr.RemoteVariable(
            name         = 'TrigBurst',
            description  = 'Used to burst N number of trigger frames from local triggering',
            offset       = 0x8,
            bitSize      = 32,
            bitOffset    = 0,
            mode         = 'WO',
        ))

        self.add(pr.RemoteVariable(
            name         = 'ContinuousMode',
            description  = 'Sets local triggering into continuous trigger mode',
            offset       = 0xC,
            bitSize      = 1,
            bitOffset    = 0,
            mode         = 'RW',
        ))
